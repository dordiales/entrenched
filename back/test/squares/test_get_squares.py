from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.squares import SquaresRepository


def test_should_return_state_of_the_game():
    squares_repository = SquaresRepository(temp_file())
    app = create_app(repositories={"squares": squares_repository})
    client = app.test_client()

    sql = """
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
            ("B7", null, null, "01"),
            ("B8", null, null, "01"),
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
            ("E6", null, null, "01"),
            ("E7", null, null, "01"),
            ("E8", null, null, "01"),
            ("E9", null, null, "01")
        """
    conn = squares_repository.create_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    response = client.get("/api/board/01")

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
