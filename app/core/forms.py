from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, SelectField, StringField
from wtforms.validators import DataRequired


class AddFoodForm(FlaskForm):
    name = StringField("Food Name", validators=[DataRequired()])
    protein = IntegerField("Protein", validators=[DataRequired()])
    carbohydrates = IntegerField("Carbohydrates", validators=[DataRequired()])
    fat = IntegerField("Fat", validators=[DataRequired()])


class AddDay(FlaskForm):
    day = DateField("New Day", validators=[DataRequired()])


class FoodDateForm(FlaskForm):
    food = SelectField(validate_choice=[DataRequired()], coerce=int)
