import sqlite3
from src.domain.errors import SlotFullError


class Game:
    def __init__(self, id, active_player="player_1", player_1=None, player_2=None):
        self.id = id
        self.active_player = active_player
        self.player_1 = player_1
        self.player_2 = player_2

    def to_dict(self):
        return {"id": self.id, "active_player": self.active_player}

    def state(self):
        return {
            "active_player": self.active_player,
            "player_1": self.player_1,
            "player_2": self.player_2,
        }


class GamesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            CREATE TABLE IF NOT EXISTS games (
                id VARCHAR PRIMARY KEY,
                active_player VARCHAR,
                player_1 Varchar,
                player_2 Varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def start_game(self, id):
        game = """INSERT INTO games (id, active_player) VALUES
        (:id, "player_1")"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(game, {"id": id})
        conn.commit()

    def get_game(self, id):
        sql = """SELECT * FROM games WHERE id=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()
        if data is None:
            return None
        game = Game(**data)
        return game

    def join(self, game_id, player_dict):
        player = player_dict["player"]
        user_name = player_dict["name"]
        game_state = self.get_game(game_id).state()
        if game_state[player] is None:
            sql = f"""UPDATE games SET {player} = :name
                    WHERE id = :id AND {player} is NULL"""
            conn = self.create_conn()
            cursor = conn.cursor()
            cursor.execute(sql, {"name": user_name, "id": game_id})
            conn.commit()
        else:
            raise SlotFullError

    def exit_game(self, game_id, player_dict):
        player = player_dict["player"]
        sql = f"""UPDATE games SET {player} = null
                WHERE id = :id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": game_id})
        conn.commit()

    def alternate_active_player(self, gameId):
        game_state = self.get_game(gameId)

        if game_state.active_player == "player_1":
            sql = """UPDATE games
                    SET active_player = 'player_2'
                    WHERE id = :id"""
        else:
            sql = """UPDATE games
                    SET active_player = 'player_1'
                    WHERE id = :id"""

        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": gameId})
        conn.commit()
