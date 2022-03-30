from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.squares import SquaresRepository


def test_should_return_state_of_the_game():
    squares_repository = SquaresRepository(temp_file())
    app = create_app(repositories={"squares": squares_repository})
    client = app.test_client()

    squares_repository.test_start()

    response = client.get("/api/game")

    assert response.json == [
        {"square": "A1", "soldier": "trooper", "player": "player_1"},
        {"square": "A2", "soldier": "trooper", "player": "player_1"},
        {"square": "A3", "soldier": None, "player": None},
        {"square": "A4", "soldier": "trooper", "player": "player_1"},
        {"square": "A5", "soldier": None, "player": None},
        {"square": "A6", "soldier": None, "player": None},
        {"square": "A7", "soldier": "trooper", "player": "player_1"},
        {"square": "A8", "soldier": None, "player": None},
        {"square": "A9", "soldier": None, "player": None},
        {"square": "B1", "soldier": None, "player": None},
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
        {"square": "D7", "soldier": "trooper", "player": "player_2"},
        {"square": "D8", "soldier": "trooper", "player": "player_1"},
        {"square": "D9", "soldier": None, "player": None},
        {"square": "E1", "soldier": None, "player": None},
        {"square": "E2", "soldier": None, "player": None},
        {"square": "E3", "soldier": None, "player": None},
        {"square": "E4", "soldier": "trooper", "player": "player_2"},
        {"square": "E5", "soldier": None, "player": None},
        {"square": "E6", "soldier": None, "player": None},
        {"square": "E7", "soldier": None, "player": None},
        {"square": "E8", "soldier": None, "player": None},
        {"square": "E9", "soldier": None, "player": None},
    ]
