from flask import Flask, Blueprint, render_template, jsonify

app = Flask(__name__, static_folder='../static', template_folder='../templates')
# static_folder='../static/dist' or static_folder='../' doesn't work, don't know why

base_bp = Blueprint('base', __name__, url_prefix='/')

@base_bp.route('/', defaults={'path': ''})
@base_bp.route('/<path:path>')
def index(path):

    return render_template('index.html')
