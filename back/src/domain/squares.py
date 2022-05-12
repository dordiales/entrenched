import sqlite3
from src.domain.soldiers import Soldier


class Square:
    def __init__(self, square, soldier, player):
        self.square = square
        self.soldier = soldier
        self.player = player

    def to_dict(self):
        return {"square": self.square, "soldier": self.soldier, "player": self.player}


class SquaresRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            CREATE TABLE IF NOT EXISTS squares (
                square VARCHAR PRIMARY KEY,
                soldier VARCHAR,
                player VARCHAR,
                game VARCHAR,
                FOREIGN KEY (game) REFERENCES games(id)
                ON DELETE CASCADE
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def start_game(self, game_id):
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(starting_state, {"id": game_id})
        conn.commit()

    def get_squares(self, game_id):
        sql = """SELECT * FROM squares WHERE game = :game_id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"game_id": game_id})

        data = cursor.fetchall()

        result = []
        for item in data:
            square = Square(
                square=item["square"], soldier=item["soldier"], player=item["player"]
            )
            result.append(square)

        return result

    def get_content(self, square):
        sql = """SELECT * FROM squares WHERE square = :square"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"square": square})

        data = cursor.fetchone()
        this_square = Square(
            square=data["square"], soldier=data["soldier"], player=data["player"]
        )
        return this_square

    def execute_move(self, origin, destination):
        origin_content = self.get_content(origin)

        conn = self.create_conn()
        cursor = conn.cursor()

        sql_movement = """UPDATE squares SET soldier= ?, player = ? WHERE square = ?"""
        cursor.execute(
            sql_movement, (origin_content.soldier, origin_content.player, destination)
        )

        update_origin = (
            """UPDATE squares SET soldier= null, player = null WHERE square = ?"""
        )
        cursor.execute(update_origin, (origin,))

        conn.commit()

    def execute_assault(self, origin, destination):
        origin_content = self.get_content(origin)
        destination_content = self.get_content(destination)

        conn = self.create_conn()
        cursor = conn.cursor()

        attacker = Soldier(origin_content.soldier)
        defender = Soldier(destination_content.soldier)

        result = attacker.engage(defender)
        print(result)
        update_origin = ""
        update_destination = ""
        if result == "draw":
            update_origin = (
                """UPDATE squares SET soldier= null, player = null WHERE square = ?"""
            )
            update_destination = (
                """UPDATE squares SET soldier= null, player = null WHERE square = ?"""
            )
            cursor.execute(update_origin, (origin,))
            cursor.execute(update_destination, (destination,))

        if result == "win":
            update_origin = (
                """UPDATE squares SET soldier= null, player = null WHERE square = ?"""
            )
            update_destination = (
                """UPDATE squares SET soldier= ?, player = ? WHERE square = ?"""
            )
            cursor.execute(update_origin, (origin,))
            cursor.execute(
                update_destination,
                (origin_content.soldier, origin_content.player, destination),
            )

        if result == "lose":
            update_origin = (
                """UPDATE squares SET soldier= null, player = null WHERE square = ?"""
            )
            cursor.execute(update_origin, (origin,))

        conn.commit()

        return result

    def is_valid_movement(self, origin, destination):
        adjacent_rules = {
            "A1": ["B1", "A2"],
            "A2": ["A1", "B2", "A3"],
            "A3": ["A2", "B3", "A4"],
            "A4": ["A3", "B4", "A5"],
            "A5": ["A4", "B5", "A6"],
            "A6": ["A5", "B6", "A7"],
            "A7": ["A6", "B7", "A8"],
            "A8": ["A7", "B8", "A9"],
            "A9": ["A8", "B9"],
            "B1": ["C1", "B2", "A1"],
            "B2": ["B1", "C2", "B3", "A2"],
            "B3": ["B2", "C3", "B4", "A3"],
            "B4": ["B3", "C4", "B5", "A4"],
            "B5": ["B4", "C5", "B6", "A5"],
            "B6": ["B5", "C6", "B7", "A6"],
            "B7": ["B6", "C7", "B8", "A7"],
            "B8": ["B7", "C8", "B9", "A8"],
            "B9": ["B8", "C9", "A9"],
            "C1": ["D1", "C2", "B1"],
            "C2": ["C1", "D2", "C3", "B2"],
            "C3": ["C2", "D3", "C4", "B3"],
            "C4": ["C3", "D4", "C5", "B4"],
            "C5": ["C4", "D5", "C6", "B5"],
            "C6": ["C5", "D6", "C7", "B6"],
            "C7": ["C6", "D7", "C8", "B7"],
            "C8": ["C7", "D8", "C9", "B8"],
            "C9": ["C8", "D9", "B9"],
            "D1": ["E1", "D2", "C1"],
            "D2": ["D1", "E2", "D3", "C2"],
            "D3": ["D2", "E3", "D4", "C3"],
            "D4": ["D3", "E4", "D5", "C4"],
            "D5": ["D4", "E5", "D6", "C5"],
            "D6": ["D5", "E6", "D7", "C6"],
            "D7": ["D6", "E7", "D8", "C7"],
            "D8": ["D7", "E8", "D9", "C8"],
            "D9": ["D8", "E9", "C9"],
            "E1": ["E2", "D1"],
            "E2": ["E1", "E3", "D2"],
            "E3": ["E2", "E4", "D3"],
            "E4": ["E3", "E5", "D4"],
            "E5": ["E4", "E6", "D5"],
            "E6": ["E5", "E7", "D6"],
            "E7": ["E6", "E8", "D7"],
            "E8": ["E7", "E9", "D8"],
            "E9": ["E8", "D9"],
        }

        if destination in adjacent_rules[origin]:
            return True
        else:
            return False


starting_state = """
            INSERT INTO squares (square, soldier, player, game) VALUES
            ("A1", "trooper", "player_1", :id),
            ("A2", "grenadier", "player_1", :id),
            ("A3", "machinegun", "player_1", :id),
            ("A4", "hq", "player_1", :id),
            ("A5", "grenadier", "player_1", :id),
            ("A6", "machinegun", "player_1", :id),
            ("A7", "trooper", "player_1", :id),
            ("A8", "grenadier", "player_1", :id),
            ("A9", "machinegun", "player_1", :id),
            ("B1", null, null, :id),
            ("B2", null, null, :id),
            ("B3", null, null, :id),
            ("B4", "trooper", "player_1", :id),
            ("B5", null, null, :id),
            ("B6", null, null, :id),
            ("B7", null, null, :id),
            ("B8", null, null, :id),
            ("B9", null, null, :id),
            ("C1", null, null, :id),
            ("C2", null, null, :id),
            ("C3", null, null, :id),
            ("C4", null, null, :id),
            ("C5", null, null, :id),
            ("C6", null, null, :id),
            ("C7", null, null, :id),
            ("C8", null, null, :id),
            ("C9", null, null, :id),
            ("D1", null, null, :id),
            ("D2", null, null, :id),
            ("D3", null, null, :id),
            ("D4", null, null, :id),
            ("D5", null, null, :id),
            ("D6", "trooper", "player_2", :id),
            ("D7", null, null, :id),
            ("D8", null, null, :id),
            ("D9", null, null, :id),
            ("E1", "machinegun", "player_2", :id),
            ("E2", "grenadier", "player_2", :id),
            ("E3", "trooper", "player_2", :id),
            ("E4", "machinegun", "player_2", :id),
            ("E5", "grenadier", "player_2", :id),
            ("E6", "hq", "player_2", :id),
            ("E7", "machinegun", "player_2", :id),
            ("E8", "grenadier", "player_2", :id),
            ("E9", "trooper", "player_2", :id)
        """
