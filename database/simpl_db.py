import sqlite3


# connection = sqlite3.connect("db.sqlite")
class Database:
    def __init__(self, path):
        self.path = path

    def create_table(self):
        with sqlite3.connect(self.path) as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS survey_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    phone_number INTEGER,
                    visit_date INTEGER,
                    food_rating TEXT,
                    cleanliness_rating TEXT, 
                    extra_comments TEXT 
                )
            """)

            connection.commit()


database = Database("db.sqlite")
database.create_table()
