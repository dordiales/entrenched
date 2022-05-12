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


def test_api_should_create_new_game():

    client = setup()

    new_game = {"gameId": "01"}

    post_response = client.post("/api/games", json=new_game)

    assert post_response.status_code == 201

    get_response = client.get("/api/games/01")

    assert get_response.json == {"active_player": "player_1"}


def test_api_should_create_new_board_when_starting_new_game():
    client = setup()

    new_game = {"gameId": "01"}

    post_response = client.post("/api/games", json=new_game)

    assert post_response.status_code == 201

    get_response = client.get("/api/board/01")

    assert get_response.json == [
        {"square": "A1", "soldier": "trooper", "player": "player_1"},
        {"square": "A2", "soldier": "grenadier", "player": "player_1"},
        {"square": "A3", "soldier": "machinegun", "player": "player_1"},
        {"square": "A4", "soldier": "hq", "player": "player_1"},
        {"square": "A5", "soldier": "grenadier", "player": "player_1"},
        {"square": "A6", "soldier": "machinegun", "player": "player_1"},
        {"square": "A7", "soldier": "trooper", "player": "player_1"},
        {"square": "A8", "soldier": "grenadier", "player": "player_1"},
        {"square": "A9", "soldier": "machinegun", "player": "player_1"},
        {"square": "B1", "soldier": None, "player": None},
        {"square": "B2", "soldier": None, "player": None},
        {"square": "B3", "soldier": None, "player": None},
        {"square": "B4", "soldier": "trooper", "player": "player_1"},
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
        {"square": "D6", "soldier": "trooper", "player": "player_2"},
        {"square": "D7", "soldier": None, "player": None},
        {"square": "D8", "soldier": None, "player": None},
        {"square": "D9", "soldier": None, "player": None},
        {"square": "E1", "soldier": "machinegun", "player": "player_2"},
        {"square": "E2", "soldier": "grenadier", "player": "player_2"},
        {"square": "E3", "soldier": "trooper", "player": "player_2"},
        {"square": "E4", "soldier": "machinegun", "player": "player_2"},
        {"square": "E5", "soldier": "grenadier", "player": "player_2"},
        {"square": "E6", "soldier": "hq", "player": "player_2"},
        {"square": "E7", "soldier": "machinegun", "player": "player_2"},
        {"square": "E8", "soldier": "grenadier", "player": "player_2"},
        {"square": "E9", "soldier": "trooper", "player": "player_2"},
    ]
