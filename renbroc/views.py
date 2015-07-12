from flask import g, render_template, session, flash, request, redirect, url_for, Response, send_file, make_response
from flask.ext.security import login_required, current_user, logout_user
from flask.ext.login import login_user, logout_user, current_user, login_required

from renbroc import app

from renbroc import db, lm

import datetime

from renbroc.forms import LoginForm

from models import *

from werkzeug import secure_filename

@app.route('/register' , methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(username=request.form['username'] , password=request.form['password'], id="37")
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return redirect(url_for('index'))


# index view function suppressed for brevity
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    logout_user()
    # if g.user is not None and g.user.is_authenticated():
    #     return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        login_user(User.query.filter_by(username=request.form['username'],password=request.form['password']))
        return redirect(url_for('user_page'))
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

    return render_template('index.html')

@app.route("/user_page")
#@login_required
def user_page():
    under_urls = db.session.query(Url).join(Url.newswhip)\
        .filter(Url.visit_count >= 50)\
        .filter(Url.comment_count >= (Url.visit_count * 10))\
        .order_by(desc(Url.comment_count))

    articles = under_urls[:5]

    return render_template('user_page.html', articles=articles)



@app.route('/', methods=['GET', 'POST'])
# @login_required
def index():
    user = g.user
    if g.user is not None and g.user.is_authenticated():
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

    print 'Test DB page'

    urls = db.session.query(Url).limit(10)

    comments = db.session.query(Comment).limit(50)

    under_urls = db.session.query(Url).join(Url.newswhip)\
        .filter(Url.visit_count >= 50)\
        .filter(Url.comment_count >= (Url.visit_count / 2))\
        .order_by(Url.visit_count)


    return render_template("test.html",
        under_urls=under_urls,
        urls=urls)


@app.route('/nltk', methods=['GET', 'POST'])
#@login_required
def nltk():
    """
    words n shit
    """

    print 'NLTK in python'

    # urls = db.session.query(Url).limit(10)

    comments = db.session.query(Newswhip).limit(20)
    print comments[:]


    # under_urls = db.session.query(Url).join(Url.newswhip)\
    #     .filter(Url.visit_count >= 50)\
    #     .filter(Url.comment_count >= (Url.visit_count / 2))\
    #     .order_by(Url.visit_count)


    return render_template("nltk.html", 
        comments=comments
        # urls=urls
        )



@app.route('/under_urls/<visit_count>/<breakoff>', methods=['GET', 'POST'])
#@login_required
def under_urls(visit_count=50, breakoff=0.5):
    """
    Test database interaction
    """

    print 'Underappretiated page'

    under_urls = db.session.query(Url).join(Url.newswhip)\
        .filter(Url.visit_count >= visit_count)\
        .filter(Url.comment_count >= (Url.visit_count * breakoff))\
        .order_by(Url.visit_count)

    print under_urls

    print under_urls[0].newswhip

    return render_template("urls.html",
        urls=under_urls)


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
