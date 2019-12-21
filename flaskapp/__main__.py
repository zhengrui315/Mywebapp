from flaskapp.routes import app

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

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True

    host = get_env_var('HOST')
    port = get_env_var('PORT')
    app.run(host=host, port=port)