import sqlite3

class ProjectModel:
    @staticmethod
    def create_connection():
        return sqlite3.connect('projects.db')

    @staticmethod
    def create_table():
        conn = ProjectModel.create_connection()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT,
            status TEXT,
            manager TEXT
        )''')
        conn.commit()
        conn.close()

    @staticmethod
    def add_project(project_name, start_date, end_date, status, manager):
        conn = ProjectModel.create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO projects (project_name, start_date, end_date, status, manager)
            VALUES (?, ?, ?, ?, ?)
        ''', (project_name, start_date, end_date, status, manager))
        conn.commit()
        conn.close()

    @staticmethod
    def update_project(project_id, project_name, start_date, end_date, status, manager):
        conn = ProjectModel.create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE projects
            SET project_name = ?, start_date = ?, end_date = ?, status = ?, manager = ?
            WHERE id = ?
        ''', (project_name, start_date, end_date, status, manager, project_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_project(project_id):
        conn = ProjectModel.create_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_projects(start_date=None, end_date=None, status=None, manager=None):
        conn = ProjectModel.create_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM projects WHERE 1=1"
        params = []

        if start_date:
            query += " AND start_date >= ?"
            params.append(start_date)
        if end_date:
            query += " AND end_date <= ?"
            params.append(end_date)
        if status:
            query += " AND status = ?"
            params.append(status)
        if manager:
            query += " AND manager LIKE ?"
            params.append(f"%{manager}%")

        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()
        conn.close()
        return rows
    
    @staticmethod
    def get_project(id):
        conn = ProjectModel.create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects WHERE id=?", (id,))
        row = cursor.fetchone()
        conn.close()
        return row if row else None
