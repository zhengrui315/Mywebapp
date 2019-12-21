from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<html><body> Welcome to my homepage </body></html>'


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    # app.config['JSON_SORT_KEYS'] = False
    app.run(host='0.0.0.0', port=5000)