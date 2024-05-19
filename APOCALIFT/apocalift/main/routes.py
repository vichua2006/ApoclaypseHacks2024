from flask import render_template, request, Blueprint, jsonify
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
    coordinate = "12.34.56"   
    longitude = "12345"
    latidude = "765432"
    return render_template('test_control.html', title='test control', power=power, coordinate=coordinate, longitude=longitude, latitude=latidude)

@main.route("/receive_keypress", methods=['POST'])
def receive_keypress():
    data = request.get_json() # retrieve the data sent from JavaScript 
    # process the data using Python code 
    print(data)
    return jsonify(result=data)