from flask import Flask
import os
from . import portafolio


def create_app():
    app = Flask(__name__)
    app.run(debug=True)

    # Setteamos la configuracion para utilizar mas tarde
    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get('SENDGRID_KEY'),
    )

    app.register_blueprint(portafolio.bp)

    return app
