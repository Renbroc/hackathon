from flask import g, render_template, session, flash, request, redirect, url_for, Response, send_file, make_response
from flask.ext.security import login_required, current_user, logout_user

from renbroc import app

from renbroc import db

import datetime

from renbroc.forms import LoginForm

from models import *

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

@app.route("/user_page")
#@login_required
def user_page():

    return render_template('user_page.html')



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

@app.route('/db_test', methods=['GET', 'POST'])
#@login_required
def db_test():
    """
    Test database interaction
    """

    print 'Test DB page'

    urls = db.session.query(Url).limit(10)
    
    comments = db.session.query(Comment).limit(50)

    xxx_urls = db.session.query(Url).join(Url.clicks_agg).filter(MemTwitterMessageUserSet.msg_date.in_(date_list)).filter(DataShingleSearch.shingle.like('%'+search_string+'%')).order_by(desc('count')).group_by(DataShingleSearch.id)

    yyy_urls = db.session.query(Url).join(Url.clicks_agg)\
        .filter(Url.comment_count >= 5)\
        .order_by(Url.comment_count)


    return render_template("test.html", 
        comments=comments,
        urls=urls)




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
