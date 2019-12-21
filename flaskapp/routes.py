from flask import Flask, render_template

app = Flask(__name__, static_folder='../static', template_folder='../templates')
# static_folder='../static/dist' or static_folder='../' doesn't work, don't know why

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    print("welcome!")
    return render_template('index.html')