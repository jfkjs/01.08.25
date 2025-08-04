import sqlite3

class DB_Manager:
    def __init__(self, database):
        self.database = database # имя базы данных
        
    def create_tables(self):
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE projects (
                project_id INTEGER PRIMARY KEY,
                user_id INTEGER,
                project_name TEXT NOT NULL,
                description TEXT,
                url TEXT,
                status_id INTEGER,
                FOREIGN KEY(status_id) REFERENCES status(status_id))
        ''')

        cur.execute('''
            CREATE TABLE status (
                status_id INTEGER PRIMARY KEY,
                status_name TEXT
                )
        ''')

        con.commit()
        con.close()






t = DB_Manager('projects.db')
t.create_tables()