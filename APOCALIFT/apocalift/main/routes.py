from apocalift.main.utils import *
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
    coordinate = (43.64485589208203, -79.4007881899902)
    longitude = coordinate[1]
    latitude = coordinate[0]
    return render_template('test_control.html', title='test control', power=power, coordinate=coordinate, longitude=longitude, latitude=latitude)

@main.route("/receive_keypress", methods=['POST'])
def receive_keypress():
    data = request.get_json() # retrieve the data sent from JavaScript 
    # process the data using Python code 
    print(data)
    keys = data['value']

    # 87 == 'w'
    # 65 == 'a'
    # 68 == 'd'
    w = ('87' in keys)
    a = ('65' in keys)
    d = ('68' in keys)

    speed = (SPEED_PERCENTAGE if w else '00')
    if (a ^ d): angle = (SERVO_LEFT_BOUND if a else SERVO_RIGHT_BOUND)
    else: angle = '90'

    passed_str = speed + angle

    # start the arduino
    # for some reason it cannot be started outside of the current receive_keypress() function
    ard = init_arduino()
    try:
        write_read(passed_str, ard)
    except Exception as e:
        print(f"ERROR: {e}")

    print(passed_str)

    return jsonify(result=data)
