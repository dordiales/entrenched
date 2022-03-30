from flask import Flask, request
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

    @app.route("/api/game", methods=["PUT"])
    def move_soldier():
        body = request.json
        origin = body["from"]
        destination = body["to"]
        if repositories["squares"].is_valid_movement(origin, destination):
            origin_content = repositories["squares"].get_content(origin)
            destination_content = repositories["squares"].get_content(destination)
            if (
                destination_content.player != None
                and destination_content.player != origin_content.player
            ):
                repositories["squares"].execute_assault(origin, destination)
            else:
                repositories["squares"].execute_move(origin, destination)
            return "", 200
        else:
            return "", 403

    return app
