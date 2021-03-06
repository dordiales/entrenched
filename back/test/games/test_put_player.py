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
    games_repository.start_game("01")

    return client


def test_api_should_save_the_players_that_joined_a_game():
    client = setup()
    join_player_1 = {"action": "join", "player": "player_1", "name": "paco"}

    first_put_response = client.put("/api/games/01", json=join_player_1)
    assert first_put_response.status_code == 200

    first_response = client.get("/api/games/01")

    assert first_response.json == {
        "active_player": "player_1",
        "player_1": "paco",
        "player_2": None,
    }

    join_player_2 = {"action": "join", "player": "player_2", "name": "paca"}

    second_put_response = client.put("/api/games/01", json=join_player_2)
    assert second_put_response.status_code == 200

    second_response = client.get("/api/games/01")

    assert second_response.json == {
        "active_player": "player_1",
        "player_1": "paco",
        "player_2": "paca",
    }


def test_api_should_set_to_null_the_players_that_exit_a_game():
    client = setup()
    join_player_1 = {"action": "join", "player": "player_1", "name": "paco"}
    client.put("/api/games/01", json=join_player_1)
    join_player_2 = {"action": "join", "player": "player_2", "name": "paca"}
    client.put("/api/games/01", json=join_player_2)

    exit_player_1 = {"action": "exit", "player": "player_1", "name": "paco"}

    first_put_response = client.put("/api/games/01", json=exit_player_1)
    assert first_put_response.status_code == 200

    first_response = client.get("/api/games/01")

    assert first_response.json == {
        "active_player": "player_1",
        "player_1": None,
        "player_2": "paca",
    }

    exit_player_2 = {"action": "exit", "player": "player_2", "name": "paca"}

    second_put_response = client.put("/api/games/01", json=exit_player_2)
    assert second_put_response.status_code == 200

    second_response = client.get("/api/games/01")

    assert second_response.json == {
        "active_player": "player_1",
        "player_1": None,
        "player_2": None,
    }


def test_api_should_return_409_conflict_when_trying_to_access_to_an_occupied_slot_of_a_game():
    client = setup()
    join_player_1 = {"action": "join", "player": "player_1", "name": "paco"}

    first_put_response = client.put("/api/games/01", json=join_player_1)
    assert first_put_response.status_code == 200

    repeated_join = {"action": "join", "player": "player_1", "name": "paca"}

    second_put_response = client.put("/api/games/01", json=repeated_join)
    assert second_put_response.status_code == 409

    second_response = client.get("/api/games/01")

    assert second_response.json == {
        "active_player": "player_1",
        "player_1": "paco",
        "player_2": None,
    }
