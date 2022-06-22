from http import client
from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.games import GamesRepository
from src.domain.squares import SquaresRepository


def setup():
    test_database = temp_file()
    squares_repository = SquaresRepository(test_database)
    games_repository = GamesRepository(test_database)
    app = create_app(
        repositories={"squares": squares_repository, "games": games_repository}
    )
    client = app.test_client()

    return client


def test_api_delete_an_unused_game():

    test_database = temp_file()
    squares_repository = SquaresRepository(test_database)
    games_repository = GamesRepository(test_database)
    app = create_app(
        repositories={"squares": squares_repository, "games": games_repository}
    )
    client = app.test_client()

    new_game = {"gameId": "01"}

    client.post("/api/games", json=new_game)

    squares_repository.winned_game("01")

    delete_response = client.delete("/api/games/01")

    assert delete_response.status_code == 200

    response = client.get("/api/games/01")

    assert response.status_code == 404


def test_api_should_delete_a_game_only_if_no_players_connected():
    client = setup()

    new_game = {"gameId": "01"}

    client.post("/api/games", json=new_game)

    join_player_1 = {"action": "join", "player": "player_1", "name": "paco"}

    client.put("/api/games/01", json=join_player_1)

    delete_response = client.delete("/api/games/01")

    assert delete_response.status_code == 409

    response = client.get("/api/games/01")

    assert response.status_code == 200


def test_api_should_delete_game_only_if_there_is_already_a_winner():

    client = setup()

    new_game = {"gameId": "01"}

    client.post("/api/games", json=new_game)

    delete_response = client.delete("/api/games/01")

    assert delete_response.status_code == 409

    response = client.get("/api/games/01")

    assert response.status_code == 200


def test_api_should_delete_all_squares_of_a_deleted_game():
    test_database = temp_file()
    squares_repository = SquaresRepository(test_database)
    games_repository = GamesRepository(test_database)
    app = create_app(
        repositories={"squares": squares_repository, "games": games_repository}
    )
    client = app.test_client()

    new_game = {"gameId": "01"}

    client.post("/api/games", json=new_game)

    squares_repository.winned_game("01")

    delete_response = client.delete("/api/games/01")

    assert delete_response.status_code == 200

    response = client.get("/api/board/01")

    assert response.status_code == 404
