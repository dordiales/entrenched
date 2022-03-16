from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "Esta es la API de Entrenched"

    @app.route("/api/game", methods=["GET"])
    def get_game_state():
        game_state = repositories["squares"].get_squares()
        return object_to_json(game_state)

    return app
