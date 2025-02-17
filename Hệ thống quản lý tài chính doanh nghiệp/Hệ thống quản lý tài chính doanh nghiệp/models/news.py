import sqlite3

class News:
    @staticmethod
    def create_connection():
        conn = sqlite3.connect('finance_management.db')
        return conn

    @staticmethod
    def create_table():
        conn = News.create_connection()
        sql = '''CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            date TEXT NOT NULL
        )'''
        conn.execute(sql)
        conn.commit()
        conn.close()

    @staticmethod
    def add_news(title, content, date):
        conn = News.create_connection()
        sql = '''INSERT INTO news (title, content, date) VALUES (?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, (title, content, date))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_news():
        conn = News.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM news ORDER BY date DESC")
        rows = cur.fetchall()
        conn.close()
        return rows
