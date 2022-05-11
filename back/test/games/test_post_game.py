from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.games import GamesRepository


def test_api_should_create_new_game():
    games_repository = GamesRepository(temp_file())
    app = create_app(repositories={"games": games_repository})
    client = app.test_client()

    new_game = {"gameId": "01"}

    post_response = client.post("/api/games", json=new_game)

    assert post_response.status_code == 201

    get_response = client.get("/api/games/01")

    assert get_response.json == {"active_player": "player_1"}
