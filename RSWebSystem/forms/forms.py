from flask_wtf import Form 
from wtforms import IntegerField, BooleanField
from wtforms.validators import DataRequired, NumberRange


class HomeForm(Form):
    proceed = BooleanField('proceed')

class RatingForm(Form):
    rating = IntegerField('rating', validators = [DataRequired(), NumberRange(min = 1, max = 5, message = "Please input a proper rating")])

class RestartForm(Form):
    proceed = BooleanField('proceed')