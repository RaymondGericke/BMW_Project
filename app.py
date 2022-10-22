from flask import Flask, render_template

app = Flask(__name__)

# Routes



@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')