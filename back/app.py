import sqlite3
from src.webserver import create_app
from domain.squares import SquaresRepository


database_path = "data/database.db"

repositories = {
    "squares": SquaresRepository(database_path),
}

app = create_app(repositories)

app.run(debug=True, host="0.0.0.0", port="5000")
