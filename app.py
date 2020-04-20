from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkeysecretkey123'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set-background/<mode>')
def set_background(mode):
    session['mode'] = mode
    return redirect(url_for('index'))