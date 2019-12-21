from flask import Flask, Blueprint, render_template

app = Flask(__name__, static_folder='../src', template_folder='../templates')
# static_folder='../src/dist' or static_folder='../' doesn't work, don't know why

@app.route('/')
def index():
    print("entering flask index page")
    return render_template('index.html')
    # return '<html><body> Welcome to my homepage </body></html>'