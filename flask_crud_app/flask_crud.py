import random

from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, Integer, MetaData

# flask setup
app = Flask(__name__)

# sqlalchemy + postgresql setup
db_string = "postgresql://postgres:romacab2012@localhost:5432/postgres"
db = create_engine(db_string)
meta = MetaData(db)

# define table structure
books_table = Table('books', meta,
                    Column('book_id', Integer),
                    Column('author', String),
                    Column('title', String))


# allow us to add book to db, select it from db and display on web UI
@app.route("/", methods=["GET", "POST"])
def get_post_book():
    book_input = request.form.get('book_input')

    with db.connect() as conn:
        # Create table
        if not books_table.exists(db):
            books_table.create()

        if book_input:
            # Insert book info to db
            insert_query = books_table \
                .insert() \
                .values(book_id=random.randint(1, 9999), author="J.R.R.Tolkien", title=book_input)
            conn.execute(insert_query)

        # select all books
        selection = conn.execute(books_table.select())

        # code below needed to select exact [2] element from select query, which is 'title'
        titles = []
        [titles.append(item._row[2], ) for item in selection]

    return render_template('home.html', book_output=titles)


# allow us to update exact book by title and redirect us back to /
@app.route("/update", methods=["POST"])
def update():
    with db.connect() as conn:
        new_title = request.form.get("new_title")
        old_title = request.form.get("old_title")

        # update exact book with old_title and change it to new_title value
        update_query = books_table \
            .update() \
            .where(books_table.c.title == old_title) \
            .values(title=new_title)
        conn.execute(update_query)

        # select here exact row which matches with new title
        selection = conn.execute(books_table.select().where(books_table.c.title == new_title))

        # code below needed to select exact [2] element from select query, which is 'title'
        titles = []
        [titles.append(item._row[2]) for item in selection]

    render_template('home.html', book=titles)
    return redirect("/")


# allow us to delete exact book by title and redirect us back to /
@app.route("/delete", methods=["POST"])
def delete():
    with db.connect() as conn:
        book_title = request.form.get("title")

        # select here exact row which matches with the title
        selection = conn.execute(books_table.select().where(books_table.c.title == book_title))

        # code below needed to select exact [2] element from select query, which is 'title'
        titles = []
        [titles.append(item._row[2]) for item in selection]

        # delete row filtered by title name
        delete_query = books_table \
            .delete() \
            .where(books_table.c.title == titles[0])
        conn.execute(delete_query)

    render_template('home.html', book=titles)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8009)
