from flask import g, render_template, session, flash, request, redirect, url_for, Response, send_file, make_response

from flask.ext.security import login_required, current_user, logout_user

from renbroc import app

import datetime

from renbroc.forms import LoginForm

#from models import *

from werkzeug import secure_filename


# index view function suppressed for brevity

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)

# Initialize toolbar
#from flask_debugtoolbar import DebugToolbarExtension
#toolbar = DebugToolbarExtension(app)

@app.route("/logout")
#@login_required
def logout():
    """
    Logs a user out. Template page gives option to compoletely log out of Okta.
    """

    logout_user()

    return render_template('logout.html')



@app.route('/', methods=['GET', 'POST'])
#@login_required
def index():
    """
    Main view for a student.
    """

    print 'Index page'
    user = {'nickname': 'Username'}  # fake user
    posts = []
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)


@app.errorhandler(404)
def page_not_found(e):
    """
    Standard 404
    """
    return render_template('404.html', path=app.root_path), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    Standard 500
    """
    return render_template('500.html'), 500
