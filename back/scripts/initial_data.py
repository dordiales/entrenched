def main():
    import sys

    sys.path.insert(0, "")

    from domain.squares import SquaresRepository

    database_path = "data/database.db"

    info_repository = SquaresRepository(database_path)


if __name__ == "__main__":
    main()
