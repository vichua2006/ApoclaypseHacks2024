from flask_wtf import FlaskForm
from wtforms import SubmitField
class Home(FlaskForm):
    submit = SubmitField('START')