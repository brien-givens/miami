import logging
import traceback

from flask import Flask

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def create_app(package_name=__name__):
    """
    Creates the flask app. Initialize all the required services
    :param package_name:
    :return:
    """

    # Register the flask app
    app = Flask(package_name)

    # Register all the blueprints
    register_blueprints(app)

    return app


def register_blueprints(app):
    """
    Register the blueprints for the app
    :param app
    :return:
    """
    log.info("Registering blueprints")

    from rico.app.contacts.apis import contact_apis

    blueprints = [
        contact_apis
    ]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)
