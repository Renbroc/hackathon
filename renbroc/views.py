from flask import g, render_template, session, flash, request, redirect, url_for, Response, send_file, make_response
from flask.ext.security import login_required, current_user, logout_user
from flask.ext.login import login_user, logout_user, current_user, login_required

from renbroc import app

from renbroc import db, lm

import datetime

from renbroc.forms import LoginForm

from models import *

from werkzeug import secure_filename


# index view function suppressed for brevity
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('Index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        login_user(User.query.filter_by(username=username,password=password))
        return redirect(url_for('login'))
    return render_template('login.html',
                           title='Sign In',
                           form=form)


# Initialize toolbar
#from flask_debugtoolbar import DebugToolbarExtension
#toolbar = DebugToolbarExtension(app)

@app.route("/settings")
@login_required
def settings():
    pass

@app.route("/logout")
#@login_required
def logout():
    """
    Logs a user out. Template page gives option to compoletely log out of Okta.
    """

    logout_user()

    return render_template('logout.html')

@app.route("/user_page")
#@login_required
def user_page():

    return render_template('user_page.html')



@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    user = g.user
    if user is not None and g.user.is_authenticated():
        return redirect(url_for('user_page'))
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/db_test', methods=['GET', 'POST'])
#@login_required
def db_test():
    """
    Test database interaction
    """

    print 'Index page'
    urls = db.session.query(Url).limit(10)

    return render_template("test.html", urls=urls)




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
