from telnetlib import GA


def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.squares import SquaresRepository
    from src.domain.games import GamesRepository

    database_path = "data/database.db"

    squares_repository = SquaresRepository(database_path)
    combat_start = """
            INSERT INTO squares (square, soldier, player) VALUES
            ("A1", "trooper", "player_1"),
            ("A2", "grenadier", "player_1"),
            ("A3", "machinegun", "player_1"),
            ("A4", "hq", "player_1"),
            ("A5", "grenadier", "player_1"),
            ("A6", "machinegun", "player_1"),
            ("A7", "trooper", "player_1"),
            ("A8", "grenadier", "player_1"),
            ("A9", "machinegun", "player_1"),
            ("B1", null, null),
            ("B2", null, null),
            ("B3", null, null),
            ("B4", "trooper", "player_1"),
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
            ("D6", "trooper", "player_2"),
            ("D7", null, null),
            ("D8", null, null),
            ("D9", null, null),
            ("E1", "machinegun", "player_2"),
            ("E2", "grenadier", "player_2"),
            ("E3", "trooper", "player_2"),
            ("E4", "machinegun", "player_2"),
            ("E5", "grenadier", "player_2"),
            ("E6", "hq", "player_2"),
            ("E7", "machinegun", "player_2"),
            ("E8", "grenadier", "player_2"),
            ("E9", "trooper", "player_2")
        """
    conn = squares_repository.create_conn()
    cursor = conn.cursor()
    cursor.execute(combat_start)
    conn.commit()

    games_repository = GamesRepository(database_path)

    first_game = """INSERT INTO games VALUES
                    ("01", "player_1")"""
    conn = games_repository.create_conn()
    cursor = conn.cursor()
    cursor.execute(first_game)
    conn.commit()


if __name__ == "__main__":
    main()
