# models.py

import sqlite3

class Book:
    def __init__(self, title, author, publication_year, book_id=1):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.book_id = book_id

    @staticmethod
    def connect_db():
        return sqlite3.connect('/app/db/library.db')

    @classmethod
    def create_table(cls):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER NOT NULL
        )''')
        conn.commit()
        conn.close()

    @classmethod
    def add_book(cls, title, author, publication_year):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)",
                       (title, author, publication_year))
        conn.commit()
        conn.close()

    @classmethod
    def get_all_books(cls):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        conn.close()
        return [cls(*book[1:]) for book in books]

    @classmethod
    def get_book(cls, book_id):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE book_id=?", (book_id,))
        book = cursor.fetchone()
        conn.close()
        if book:
            return cls(*book[1:])
        return None

    @classmethod
    def update_book(cls, book_id, title, author, publication_year):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute('''UPDATE books
                          SET title = ?, author = ?, publication_year = ?
                          WHERE book_id = ?''',
                       (title, author, publication_year, book_id))
        conn.commit()
        conn.close()

    @classmethod
    def delete_book(cls, book_id):
        conn = cls.connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE book_id=?", (book_id,))
        conn.commit()
        conn.close()

