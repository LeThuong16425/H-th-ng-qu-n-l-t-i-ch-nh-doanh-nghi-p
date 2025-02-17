import sqlite3

class Transaction:
    def __init__(self, id, date, amount, category, description, department):
        self.id = id
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.department = department

    @staticmethod
    def create_connection():
        conn = sqlite3.connect('finance_management.db')
        return conn

    @staticmethod
    def create_table():
        conn = Transaction.create_connection()
        sql = '''CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            amount REAL,
            category TEXT,
            description TEXT,
            department TEXT
        )'''
        conn.execute(sql)
        conn.close()

    @staticmethod
    def add_transaction(date, amount, category, description, department):
        conn = Transaction.create_connection()
        sql = '''INSERT INTO transactions(date, amount, category, description, department)
                 VALUES(?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, (date, amount, category, description, department))
        conn.commit()
        conn.close()

    @staticmethod
    def update_transaction(id, date, amount, category, description, department):
        conn = Transaction.create_connection()
        sql = '''UPDATE transactions
                 SET date = ?, amount = ?, category = ?, description = ?, department = ?
                 WHERE id = ?'''
        cur = conn.cursor()
        cur.execute(sql, (date, amount, category, description, department, id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_transaction(id):
        conn = Transaction.create_connection()
        sql = 'DELETE FROM transactions WHERE id=?'
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_transactions():
        conn = Transaction.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM transactions")
        rows = cur.fetchall()
        transactions = [Transaction(*row) for row in rows]
        conn.close()
        return transactions

    @staticmethod
    def get_transaction(id):
        conn = Transaction.create_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM transactions WHERE id=?", (id,))
        row = cur.fetchone()
        conn.close()
        return Transaction(*row) if row else None
