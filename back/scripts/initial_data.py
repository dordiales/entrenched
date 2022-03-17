def main():
    import sys

    sys.path.insert(0, "")

    from src.domain.squares import SquaresRepository

    database_path = "data/database.db"

    squares_repository = SquaresRepository(database_path)
    squares_repository.test_start()


if __name__ == "__main__":
    main()
