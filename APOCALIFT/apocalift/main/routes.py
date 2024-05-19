from flask import render_template, request, Blueprint
from apocalift.forms import Home
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    form = Home()
    return render_template('home.html', title='Home', form=form)

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/test_control")
@login_required
def test_control():
    power = "100%"
    coordinate = (43.64485589208203, -79.4007881899902)
    longitude = coordinate[1]
    latitude = coordinate[0]
    return render_template('test_control.html', title='test control', power=power, coordinate=coordinate, longitude=longitude, latitude=latitude)
