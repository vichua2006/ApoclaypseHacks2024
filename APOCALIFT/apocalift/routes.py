from flask import render_template, redirect, url_for, request, flash, abort
from apocalift import app
from apocalift.forms import Home

@app.route('/')
@app.route('/home')
def home():
    form = Home()
    return render_template('home.html', title='Home', form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/test_control')
def test_control():
    return render_template('test_control.html')