from flaskapp.routes import app


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    # app.config['JSON_SORT_KEYS'] = False
    app.run(host='0.0.0.0', port=5000)