from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.squares import SquaresRepository


def test_should_move_soldier_from_a_square_to_another():
    squares_repository = SquaresRepository(temp_file())
    app = create_app(repositories={"squares": squares_repository})
    client = app.test_client()

    squares_repository.test_start()

    movement = {"from": "A1", "to": "B1"}

    put_response = client.put("api/game", json=movement)
    assert put_response.status_code == 200

    response = client.get("/api/game")

    assert response.json[0] == {"square": "A1", "soldier": None, "player": None}
    assert response.json[9] == {
        "square": "B1",
        "soldier": "trooper",
        "player": "player_1",
    }


def test_should_move_only_to_adjacent_squares():
    squares_repository = SquaresRepository(temp_file())
    app = create_app(repositories={"squares": squares_repository})
    client = app.test_client()

    squares_repository.test_start()

    movement = {"from": "A1", "to": "B2"}

    put_response = client.put("api/game", json=movement)
    assert put_response.status_code == 403


def test_movement_to_enemy_square_should_resolve_assault():
    squares_repository = SquaresRepository(temp_file())
    app = create_app(repositories={"squares": squares_repository})
    client = app.test_client()

    squares_repository.test_start()

    movement = {"from": "D8", "to": "D7"}

    put_response = client.put("api/game", json=movement)
    assert put_response.status_code == 200

    response = client.get("/api/game")

    assert response.json[33] == {"square": "D7", "soldier": None, "player": None}
    assert response.json[34] == {"square": "D8", "soldier": None, "player": None}


def test_winned_assault_should_result_in_attacker_in_the_defender_square():
    squares_repository = SquaresRepository(temp_file())
    app = create_app(repositories={"squares": squares_repository})
    client = app.test_client()

    squares_repository.test_start()

    movement = {"from": "B7", "to": "B8"}

    put_response = client.put("api/game", json=movement)
    assert put_response.status_code == 200

    response = client.get("/api/game")

    assert response.json[15] == {"square": "B7", "soldier": None, "player": None}
    assert response.json[16] == {
        "square": "B8",
        "soldier": "trooper",
        "player": "player_1",
    }
