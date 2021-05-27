from .src.app.App import App
from .src.sql.SQLConnection import SQL

if __name__ == "__main__":
    SQLConnection = SQL()

    App(SQLConnection)
