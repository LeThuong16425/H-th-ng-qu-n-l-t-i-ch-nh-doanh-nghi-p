import sqlite3
from datetime import datetime

class NewsModel:
    @staticmethod
    def create_connection():
        return sqlite3.connect('projects.db')

    @staticmethod
    def get_news():
        conn = NewsModel.create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM news ORDER BY date DESC")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def insert_news(title, content):
        conn = NewsModel.create_connection()
        cursor = conn.cursor()
        
        # Insert the news article with the current date
        cursor.execute("INSERT INTO news (title, content, date) VALUES (?, ?, ?)",
                       (title, content, datetime.now().strftime("%Y-%m-%d")))
        
        conn.commit()
        conn.close()

def create_news_table():
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()

    # Create the news table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        date TEXT NOT NULL
    )''')

    conn.commit()
    conn.close()
    print("News table created successfully!")

def insert_sample_news():
    conn = sqlite3.connect('projects.db')
    cursor = conn.cursor()

    # Insert sample news data
    cursor.execute('''
    INSERT INTO news (title, content, date)
    VALUES
        ('Hội thảo về Quản lý Dự Án', 'Hội thảo sẽ được tổ chức vào cuối tháng này để chia sẻ về phương pháp quản lý dự án.', '2025-02-01'),
        ('Cập nhật về Dự Án Game', 'Dự án Game của chúng tôi đã hoàn thành giai đoạn phát triển beta.', '2025-02-05'),
        ('Tuyển Dụng Nhân Viên', 'Chúng tôi đang tìm kiếm những tài năng trong lĩnh vực công nghệ để gia nhập đội ngũ.', '2025-02-10');
    ''')

    conn.commit()
    conn.close()
    print("Sample news inserted successfully!")

# Run these functions to create the news table and insert sample news data
create_news_table()
insert_sample_news()
