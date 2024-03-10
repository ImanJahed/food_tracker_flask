from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for

from app.core.forms import AddDay, AddFoodForm, FoodDateForm
from app.core.models import Food, LogDate
from app.extensions import db

core_blueprint = Blueprint("core", __name__)


@core_blueprint.route("/", methods=["GET", "POST"])
def index():
    page = request.args.get("page")
    print(page)
    form = AddDay()
    if form.validate_on_submit():
        new_date = LogDate(date=form.day.data)
        db.session.add(new_date)
        db.session.commit()
        flash("New day Added", "success")
        return redirect(url_for("core.index"))

    days = LogDate.query.order_by(LogDate.date.desc()).all()
    return render_template("core/home.html", form=form, days=days, page=page)


@core_blueprint.route("/add_food", methods=["GET", "POST"])
def food():
    page = request.args.get("page")
    print(page)
    form = AddFoodForm()
    foods = Food.query.order_by(Food.date.desc()).all()
    if form.validate_on_submit():
        calories = (
            (form.protein.data * 4)
            + (form.carbohydrates.data * 4)
            + (form.fat.data * 9)
        )
        food = Food(
            name=form.name.data,
            protein=form.protein.data,
            carbohydrates=form.carbohydrates.data,
            fat=form.fat.data,
            calories=calories,
        )

        db.session.add(food)
        db.session.commit()
        flash("Food add successfully.", "success")
        return redirect(url_for("core.food"))

    return render_template("core/add_food.html", foods=foods, form=form)


@core_blueprint.route("/day/<date>", methods=["GET", "POST"])
def day(date):
    n_date = datetime.strptime(date, "%Y-%m-%d")  # 2024-03-18 2000:00:00
    date_time = LogDate.query.filter_by(date=n_date).first()
    form = FoodDateForm()
    form.food.choices = [(food.id, food.name) for food in Food.query.all()]
    total = {
        "protein": 0,
        "carbohydrates": 0,
        "fat": 0,
        "calories": 0,
    }
    for food in date_time.dates:
        total["protein"] += food.protein
        total["carbohydrates"] += food.carbohydrates
        total["fat"] += food.fat
        total["calories"] += food.calories
    print(total)
    if form.validate_on_submit():
        food = Food.query.get(form.food.data)
        food.dates.append(date_time)
        db.session.commit()
        flash("Food successfully added", "success")
        return redirect(url_for("core.day", date=date))

    return render_template("core/day.html", form=form, date_time=date_time, total=total)
