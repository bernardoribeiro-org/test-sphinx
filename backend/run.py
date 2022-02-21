""" flask app runner file"""

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from app.api import flask_api

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

flask_api.init_app(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
