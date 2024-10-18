import sqlite3


# connection = sqlite3.connect("db.system.data.sqlite")
class Database:
    def __init__(self, path):
        self.path = path

    def create_table(self):
        with sqlite3.connect(self.path) as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS survey_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    phone_number INTEGER,
                    visit_date INTEGER,
                    food_rating TEXT,
                    cleanliness_rating TEXT, 
                    extra_comments TEXT 
                    tg_id INTEGER
                )
            """)

            connection.commit()



def execute(self, query: str, params: tuple = None):
    with sqlite3.connect(self.path) as connection:
        connection.execute(query, params)
        connection.commit()
