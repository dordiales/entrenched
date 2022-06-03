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
    join_player_1 = {"player": "player_1", "name": "paco"}

    first_put_response = client.put("/api/games/01", json=join_player_1)
    assert first_put_response.status_code == 200

    first_response = client.get("/api/games/01")

    assert first_response.json == {
        "active_player": "player_1",
        "player_1": "paco",
        "player_2": None,
    }

    join_player_2 = {"player": "player_2", "name": "paca"}

    second_put_response = client.put("/api/games/01", json=join_player_2)
    assert second_put_response.status_code == 200

    second_response = client.get("/api/games/01")

    assert second_response.json == {
        "active_player": "player_1",
        "player_1": "paco",
        "player_2": "paca",
    }
