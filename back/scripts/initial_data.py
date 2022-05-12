from telnetlib import GA


def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.squares import SquaresRepository
    from src.domain.games import GamesRepository

    database_path = "data/database.db"

    games_repository = GamesRepository(database_path)
    squares_repository = SquaresRepository(database_path)

    games_repository.start_game("01")
    squares_repository.start_game("01")


if __name__ == "__main__":
    main()
