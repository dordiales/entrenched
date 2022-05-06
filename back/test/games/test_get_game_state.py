from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.games import GamesRepository


def test_game_state_should_return_active_player():
    games_repository = GamesRepository(temp_file())
    app = create_app(repositories={"games": games_repository})
    client = app.test_client()
    games_repository.start_game("01")

    response = client.get("/api/games/01")

    assert response.json == {"active_player": "player_1"}
