from flask import Flask, jsonify, request
from flask_cors import CORS

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "Esta es la API de Entrenched"

    @app.route("/api/board/<id>", methods=["GET"])
    def get_board_state(id):
        board_state = repositories["squares"].get_squares(id)
        if board_state == []:
            return "Board not found", 404

        return object_to_json(board_state)

    @app.route("/api/board/<id>", methods=["PUT"])
    def move_soldier(id):
        body = request.json
        origin = body["from"]
        destination = body["to"]
        game_id = id

        movement_result = repositories["squares"].move_soldier(
            origin, destination, game_id
        )
        if movement_result["status_code"] == 403:
            return movement_result["message"], movement_result["status_code"]

        repositories["games"].alternate_active_player(game_id)
        return movement_result["message"], movement_result["status_code"]

    @app.route("/api/games/<id>", methods=["GET"])
    def get_game_current_state(id):
        game = repositories["games"].get_game(id)
        game_state = game.state()
        return jsonify(game_state)

    @app.route("/api/games", methods=["POST"])
    def create_new_game():
        body = request.json
        game_id = body["gameId"]
        game = repositories["games"].get_game(game_id)
        if game is None:
            repositories["games"].start_game(game_id)
            repositories["squares"].start_game(game_id)
            return "Game created successfully", 201
        return "Game already exist", 307

    return app
