from flask import render_template, request, Blueprint
from apocalift.forms import Home

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    form = Home()
    return render_template('home.html', title='Home', form=form)

@main.route("/about")
def about():
    return render_template('about.html', title='About')