from flaskapp.routes import app, base_bp
from flaskapp.api_routes import api_bp
from flaskapp.model.initialization import initialize
import os


ENV_DEFAULTS = {
    'HOST': '0.0.0.0',
    'PORT': 5000,
    'FLASK_ENV': 'dev'
}

def get_env_var(varname):
    var = os.environ.get(varname)
    if not var:
        assert varname in ENV_DEFAULTS, f'{varname} is not a valid name'
        var = ENV_DEFAULTS[varname]
    return var

def configure_app(app=app):
    app.debug = True

    # set up secret key
    app.secret_key = 'super_secret_key'

    # set up database

    # register blueprint
    app.register_blueprint(base_bp)
    app.register_blueprint(api_bp)
    # set up admin


if __name__ == '__main__':
    configure_app(app)
    host = get_env_var('HOST')
    port = get_env_var('PORT')

    app.run(host=host, port=port)