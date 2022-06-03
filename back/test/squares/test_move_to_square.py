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
            INSERT INTO squares (square, soldier, player, game) VALUES
            ("A1", "trooper", "player_1", "01"),
            ("A2", "trooper", "player_1", "01"),
            ("A3", null, null, "01"),
            ("A4", "trooper", "player_1", "01"),
            ("A5", null, null, "01"),
            ("A6", null, null, "01"),
            ("A7", "trooper", "player_1", "01"),
            ("A8", null, null, "01"),
            ("A9", null, null, "01"),
            ("B1", null, null, "01"),
            ("B2", null, null, "01"),
            ("B3", null, null, "01"),
            ("B4", null, null, "01"),
            ("B5", null, null, "01"),
            ("B6", null, null, "01"),
            ("B7", "trooper", "player_1", "01"),
            ("B8", "grenadier", "player_2", "01"),
            ("B9", null, null, "01"),
            ("C1", null, null, "01"),
            ("C2", null, null, "01"),
            ("C3", null, null, "01"),
            ("C4", null, null, "01"),
            ("C5", null, null, "01"),
            ("C6", null, null, "01"),
            ("C7", null, null, "01"),
            ("C8", null, null, "01"),
            ("C9", null, null, "01"),
            ("D1", null, null, "01"),
            ("D2", null, null, "01"),
            ("D3", null, null, "01"),
            ("D4", null, null, "01"),
            ("D5", null, null, "01"),
            ("D6", null, null, "01"),
            ("D7", "trooper", "player_2", "01"),
            ("D8", "trooper", "player_1", "01"),
            ("D9", null, null, "01"),
            ("E1", null, null, "01"),
            ("E2", null, null, "01"),
            ("E3", null, null, "01"),
            ("E4", "trooper", "player_2", "01"),
            ("E5", null, null, "01"),
            ("E6", "hq", "player_2", "01"),
            ("E7", null, null, "01"),
            ("E8", null, null, "01"),
            ("E9", null, null, "01")
        """
    conn = squares_repository.create_conn()
    cursor = conn.cursor()
    cursor.execute(combat_start)
    conn.commit()

    return client


def test_should_move_soldier_from_a_square_to_another():
    client = setup()

    movement = {"from": "A1", "to": "B1"}

    put_response = client.put("api/board/01", json=movement)
    assert put_response.status_code == 200

    response = client.get("/api/board/01")

    assert response.json[0] == {"square": "A1", "soldier": None, "player": None}
    assert response.json[9] == {
        "square": "B1",
        "soldier": "trooper",
        "player": "player_1",
    }


def test_should_move_only_to_adjacent_squares():
    client = setup()

    movement = {"from": "A1", "to": "B2"}

    put_response = client.put("api/board/01", json=movement)
    assert put_response.status_code == 403


def test_draw_assault_should_result_in_both_soldiers_deleted():
    client = setup()

    movement = {"from": "D8", "to": "D7"}

    put_response = client.put("api/board/01", json=movement)
    assert put_response.status_code == 200

    response = client.get("/api/board/01")

    assert response.json[33] == {"square": "D7", "soldier": None, "player": None}
    assert response.json[34] == {"square": "D8", "soldier": None, "player": None}


def test_winned_assault_should_result_in_attacker_in_the_defender_square():
    client = setup()

    movement = {"from": "B7", "to": "B8"}

    put_response = client.put("api/board/01", json=movement)
    assert put_response.status_code == 200

    response = client.get("/api/board/01")

    assert response.json[15] == {"square": "B7", "soldier": None, "player": None}
    assert response.json[16] == {
        "square": "B8",
        "soldier": "trooper",
        "player": "player_1",
    }


def test_lost_assault_should_result_in_attacker_deleted():
    client = setup()

    movement = {"from": "B8", "to": "B7"}

    put_response = client.put("api/board/01", json=movement)
    assert put_response.status_code == 200

    response = client.get("/api/board/01")

    assert response.json[15] == {
        "square": "B7",
        "soldier": "trooper",
        "player": "player_1",
    }
    assert response.json[16] == {"square": "B8", "soldier": None, "player": None}


def test_HQ_should_not_move():
    client = setup()

    movement = {"from": "E6", "to": "E7"}

    put_response = client.put("api/board/01", json=movement)
    assert put_response.status_code == 403

    response = client.get("/api/board/01")

    assert response.json[41] == {
        "square": "E6",
        "soldier": "hq",
        "player": "player_2",
    }
    assert response.json[42] == {"square": "E7", "soldier": None, "player": None}


def test_active_player_should_alternate_after_succesfull_movement():
    client = setup()

    movement = {"from": "A1", "to": "B1"}

    put_response = client.put("api/board/01", json=movement)
    assert put_response.status_code == 200

    game_state = client.get("/api/games/01")

    assert game_state.json["active_player"] == "player_2"


def test_active_player_should_not_alternate_after_unsuccesfull_movement():
    client = setup()

    movement = {"from": "A1", "to": "B2", "gameId": "01"}
    initial_player_turn = "player_1"

    put_response = client.put("api/board/01", json=movement)
    assert put_response.status_code == 403

    final_game_state = client.get("/api/games/01")

    assert final_game_state.json["active_player"] == initial_player_turn
