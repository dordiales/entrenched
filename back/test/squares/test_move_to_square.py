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

    assert response.json == [
        {"square": "A1", "soldier": None, "player": None},
        {"square": "A2", "soldier": "rifleman", "player": "player_1"},
        {"square": "A3", "soldier": None, "player": None},
        {"square": "A4", "soldier": "rifleman", "player": "player_1"},
        {"square": "A5", "soldier": None, "player": None},
        {"square": "A6", "soldier": None, "player": None},
        {"square": "A7", "soldier": "rifleman", "player": "player_1"},
        {"square": "A8", "soldier": None, "player": None},
        {"square": "A9", "soldier": None, "player": None},
        {"square": "B1", "soldier": "rifleman", "player": "player_1"},
        {"square": "B2", "soldier": None, "player": None},
        {"square": "B3", "soldier": None, "player": None},
        {"square": "B4", "soldier": None, "player": None},
        {"square": "B5", "soldier": None, "player": None},
        {"square": "B6", "soldier": None, "player": None},
        {"square": "B7", "soldier": None, "player": None},
        {"square": "B8", "soldier": None, "player": None},
        {"square": "B9", "soldier": None, "player": None},
        {"square": "C1", "soldier": None, "player": None},
        {"square": "C2", "soldier": None, "player": None},
        {"square": "C3", "soldier": None, "player": None},
        {"square": "C4", "soldier": None, "player": None},
        {"square": "C5", "soldier": None, "player": None},
        {"square": "C6", "soldier": None, "player": None},
        {"square": "C7", "soldier": None, "player": None},
        {"square": "C8", "soldier": None, "player": None},
        {"square": "C9", "soldier": None, "player": None},
        {"square": "D1", "soldier": None, "player": None},
        {"square": "D2", "soldier": None, "player": None},
        {"square": "D3", "soldier": None, "player": None},
        {"square": "D4", "soldier": None, "player": None},
        {"square": "D5", "soldier": None, "player": None},
        {"square": "D6", "soldier": None, "player": None},
        {"square": "D7", "soldier": "rifleman", "player": "player_2"},
        {"square": "D8", "soldier": None, "player": None},
        {"square": "D9", "soldier": None, "player": None},
        {"square": "E1", "soldier": None, "player": None},
        {"square": "E2", "soldier": None, "player": None},
        {"square": "E3", "soldier": None, "player": None},
        {"square": "E4", "soldier": "rifleman", "player": "player_2"},
        {"square": "E5", "soldier": None, "player": None},
        {"square": "E6", "soldier": None, "player": None},
        {"square": "E7", "soldier": None, "player": None},
        {"square": "E8", "soldier": None, "player": None},
        {"square": "E9", "soldier": None, "player": None},
    ]


def test_should_move_only_to_adjacent_squares():
    squares_repository = SquaresRepository(temp_file())
    app = create_app(repositories={"squares": squares_repository})
    client = app.test_client()

    squares_repository.test_start()

    movement = {"from": "A1", "to": "B2"}

    put_response = client.put("api/game", json=movement)
    assert put_response.status_code == 403
