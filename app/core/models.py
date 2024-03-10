from app.extensions import db


class LogDate(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.date})"


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    protein = db.Column(db.Integer, nullable=False)
    carbohydrates = db.Column(db.Integer, nullable=False)
    fat = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Integer, nullable=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    dates = db.relationship("LogDate", secondary="food_date", backref="dates")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.name})"


db.Table(
    "food_date",
    db.Column("log_date", db.Integer, db.ForeignKey("log_date.id")),
    db.Column("food", db.Integer, db.ForeignKey("food.id")),
)
