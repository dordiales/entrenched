from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.squares import SquaresRepository


def test_should_return_state_of_the_game():
    squares_repository = SquaresRepository(temp_file())
    app = create_app(repositories={"squares": squares_repository})
    client = app.test_client()

    sql = """
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
            ("B7", null, null),
            ("B8", null, null),
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
            ("E6", null, null),
            ("E7", null, null),
            ("E8", null, null),
            ("E9", null, null)
        """
    conn = squares_repository.create_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

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
