from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm, SyringeForm
import numpy as np

def adder():
    a=np.array([0])
    np.save('a.npy', a)
    
    

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Farzad'}
    posts = [
        {
            'author': {'nickname': 'UTRENTO'},
            'body': 'Perfect !'
        },
        {
            'author': {'nickname': 'UGlasgow'},
            'body': 'Problems!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.route('/liveview', methods=['GET', 'POST'])
def liveview():
    form = SyringeForm()
    if form.validate_on_submit():
        flash('Syringe Down="%s", Plunger Pull=%s' %
              (form.syringe.data, form.plunger.data))
        adder()
        return redirect('/index')
    return render_template('liveview.html',
                           title='Live View',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])





