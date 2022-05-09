from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.squares import SquaresRepository
from src.domain.games import GamesRepository


def setup():
    test_database = temp_file()
    squares_repository = SquaresRepository(test_database)
    games_repository = GamesRepository(test_database)
    app = create_app(
        repositories={"squares": squares_repository, "games": games_repository}
    )
    client = app.test_client()

    games_repository.start_game("01")

    combat_start = """
            INSERT INTO squares (square, soldier, player) VALUES
            ("A1", "trooper", "player_1"),
            ("A2", "trooper", "player_1"),
            ("A3", null, null),
            ("A4", "trooper", "player_1"),
            ("A5", null, null),
            ("A6", null, null),
            ("A7", "trooper", "player_1"),
            ("A8", null, null),
            ("A9", null, null),
            ("B1", null, null),
            ("B2", null, null),
            ("B3", null, null),
            ("B4", null, null),
            ("B5", null, null),
            ("B6", null, null),
            ("B7", "trooper", "player_1"),
            ("B8", "grenadier", "player_2"),
            ("B9", null, null),
            ("C1", null, null),
            ("C2", null, null),
            ("C3", null, null),
            ("C4", null, null),
            ("C5", null, null),
            ("C6", null, null),
            ("C7", null, null),
            ("C8", null, null),
            ("C9", null, null),
            ("D1", null, null),
            ("D2", null, null),
            ("D3", null, null),
            ("D4", null, null),
            ("D5", null, null),
            ("D6", null, null),
            ("D7", "trooper", "player_2"),
            ("D8", "trooper", "player_1"),
            ("D9", null, null),
            ("E1", null, null),
            ("E2", null, null),
            ("E3", null, null),
            ("E4", "trooper", "player_2"),
            ("E5", null, null),
            ("E6", "hq", "player_2"),
            ("E7", null, null),
            ("E8", null, null),
            ("E9", null, null)
        """
    conn = squares_repository.create_conn()
    cursor = conn.cursor()
    cursor.execute(combat_start)
    conn.commit()

    return client


def test_should_move_soldier_from_a_square_to_another():
    client = setup()

    movement = {"from": "A1", "to": "B1", "gameId": "01"}

    put_response = client.put("api/board", json=movement)
    assert put_response.status_code == 200

    response = client.get("/api/board")

    assert response.json[0] == {"square": "A1", "soldier": None, "player": None}
    assert response.json[9] == {
        "square": "B1",
        "soldier": "trooper",
        "player": "player_1",
    }


def test_should_move_only_to_adjacent_squares():
    client = setup()

    movement = {"from": "A1", "to": "B2", "gameId": "01"}

    put_response = client.put("api/board", json=movement)
    assert put_response.status_code == 403


def test_draw_assault_should_result_in_both_soldiers_deleted():
    client = setup()

    movement = {"from": "D8", "to": "D7", "gameId": "01"}

    put_response = client.put("api/board", json=movement)
    assert put_response.status_code == 200

    response = client.get("/api/board")

    assert response.json[33] == {"square": "D7", "soldier": None, "player": None}
    assert response.json[34] == {"square": "D8", "soldier": None, "player": None}


def test_winned_assault_should_result_in_attacker_in_the_defender_square():
    client = setup()

    movement = {"from": "B7", "to": "B8", "gameId": "01"}

    put_response = client.put("api/board", json=movement)
    assert put_response.status_code == 200

    response = client.get("/api/board")

    assert response.json[15] == {"square": "B7", "soldier": None, "player": None}
    assert response.json[16] == {
        "square": "B8",
        "soldier": "trooper",
        "player": "player_1",
    }


def test_lost_assault_should_result_in_attacker_deleted():
    client = setup()

    movement = {"from": "B8", "to": "B7", "gameId": "01"}

    put_response = client.put("api/board", json=movement)
    assert put_response.status_code == 200

    response = client.get("/api/board")

    assert response.json[15] == {
        "square": "B7",
        "soldier": "trooper",
        "player": "player_1",
    }
    assert response.json[16] == {"square": "B8", "soldier": None, "player": None}


def test_HQ_should_not_move():
    client = setup()

    movement = {"from": "E6", "to": "E7", "gameId": "01"}

    put_response = client.put("api/board", json=movement)
    assert put_response.status_code == 403

    response = client.get("/api/board")

    assert response.json[41] == {
        "square": "E6",
        "soldier": "hq",
        "player": "player_2",
    }
    assert response.json[42] == {"square": "E7", "soldier": None, "player": None}


def test_active_player_should_alternate_after_succesfull_movement():
    client = setup()

    movement = {"from": "A1", "to": "B1", "gameId": "01"}

    put_response = client.put("api/board", json=movement)
    assert put_response.status_code == 200

    game_state = client.get("/api/games/01")

    assert game_state.json == {"active_player": "player_2"}


def test_active_player_should_not_alternate_after_unsuccesfull_movement():
    client = setup()

    movement = {"from": "A1", "to": "B2", "gameId": "01"}
    initial_game_state = {"active_player": "player_1"}

    put_response = client.put("api/board", json=movement)
    assert put_response.status_code == 403

    final_game_state = client.get("/api/games/01")

    assert final_game_state.json == initial_game_state
