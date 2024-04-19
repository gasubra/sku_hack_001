import os
import enum
import traceback
from typing import Union, Dict, Any, List

from flask import Flask, g, jsonify
import logging
from flask.json.provider import DefaultJSONProvider
from flask.logging import default_handler
#from logging import Formatter
#from logging import Formatter, StreamHandler
import flask
from flask_cors import CORS

from sku_hack_001.routes.blueprint import sku_blueprint

def _local_configuration_path() -> str:
    """Returns the path to the local configuration directory."""
    print("****************", os.path.join(os.path.split(__file__)[0], "config"))
    return os.path.join(os.path.split(__file__)[0], "config")

def create_application(test_config: dict = None) -> Flask:
    """Create and configure the application."""
    # pylint: disable=invalid-name
    app = Flask(__name__, instance_relative_config=True)  # type: ignore


    # set up configurations
    if os.getenv('FLASK_ENV') == 'production':
        app.config.from_object('config.ProductionConfig')
    elif os.getenv('FLASK_ENV') == 'testing':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    return app


app = create_application()
app.register_blueprint(sku_blueprint, url_prefix="/skus")



if __name__ == '__main__':
    app.run()