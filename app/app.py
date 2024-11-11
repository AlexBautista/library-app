# app.py

from flask import Flask, render_template, request, redirect, url_for
from models import Book

app = Flask(__name__)

# Create the database table if it doesn't exist
Book.create_table()

@app.route('/')
def index():
      books = Book.get_all_books()
      print(books)
      return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publication_year = request.form['publication_year']
        Book.add_book(title, author, publication_year)
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/update/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    book = Book.get_book(book_id)
    if not book:
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publication_year = request.form['publication_year']
        Book.update_book(book_id, title, author, publication_year)
        return redirect(url_for('index'))
    
    return render_template('update_book.html', book=book)

@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    Book.delete_book(book_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

