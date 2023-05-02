import sqlite3
from werkzeug.security import generate_password_hash

books_DB_path = r'App/Data/Books_DB.db'
# books_DB_path = r'App\Data\Books_DB.db'

# General
def connect_to_db():
    # Connect
    con = sqlite3.connect(books_DB_path)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    return con,cur


def get_all_the_objects_from_db(table='Books'):
    # Connect
    con ,cur = connect_to_db()
    # get all the books
    result = cur.execute(f'SELECT * from {table}').fetchall()    
    # close
    con.close()
    return result


def get_an_object_from_db_with_id(id_pk, table='Books'):
    # Connect
    con ,cur = connect_to_db()
    # get a book 
    result = cur.execute(f'SELECT * from {table} WHERE id={id_pk}').fetchone()
    # close
    con.close()
    return result


def del_an_object_from_db(id_pk, table="Books"):
    print("object has been deleted from db - Done.")
    # Connect
    con ,cur = connect_to_db()
    # delete a book
    cur.execute(f'DELETE from {table} WHERE id="{id_pk}"')
    con.commit()
    # close
    con.close()


# Books
def add_book_to_data(book, price, picture):
    # Connect
    con ,cur = connect_to_db()
    # add book
    cur.execute(f'INSERT INTO Books("Book", "Price", "Picture") VALUES("{book}","{price}","{picture}")')
    con.commit()
    # close
    con.close()


def search_by_book_name(book_name):
    # Connect
    con ,cur = connect_to_db()
    # search by book name
    results = cur.execute(f"SELECT * FROM Books WHERE Book LIKE '{book_name}%'").fetchall()
    print(results)
    # close
    con.close()
    return results


# Users
def get_user(username):
    # Connect
    con ,cur = connect_to_db()
    # get data
    result = cur.execute(f'SELECT * from Users WHERE username="{username}"').fetchone()
    # close
    con.close()
    return result


def add_user_to_data(username, eml, pet_name, password, permissions= 'customer'):
    # Connect
    con ,cur = connect_to_db()
    # hash password
    pass_hash = generate_password_hash(password)
    # add user
    cur.execute(
        f"INSERT INTO Users ('username', 'email', 'pet_name', 'password', 'permissions') VALUES ('{username}', '{eml}', '{pet_name}', '{pass_hash}', '{permissions}')")
    con.commit()
    # close
    con.close()


def change_user_pass(password, id_pk):
    # Connect
    con ,cur = connect_to_db()
    # hash password
    pass_hash = generate_password_hash(password)
    # change pass
    cur.execute(f"UPDATE Users SET password='{pass_hash}' WHERE id='{id_pk}'")
    con.commit()
    # close
    con.close()


def change_user_permission(permission, id_pk):
    # Connect
    con ,cur = connect_to_db()
    # change pass
    cur.execute(f"UPDATE Users SET permissions='{permission}' WHERE id='{id_pk}'")
    con.commit()
    # close
    con.close()


def user_loans(user_id):
    # Connect
    con ,cur = connect_to_db()
    # check loans
    loans = cur.execute(f"SELECT * FROM Loans WHERE user_id= '{user_id}' AND returned='False'").fetchall()
    # close
    con.close()
    return loans


# Loans
def add_loan_in_db(loan_date, return_date, book_id, user_id, returned=False):
    # Connect
    con ,cur = connect_to_db()
    # add loan
    cur.execute(f'INSERT INTO Loans("loan_date", "return_date", "returned", "book_id", "user_id") VALUES("{loan_date}","{return_date}","{returned}","{book_id}","{user_id}")')
    con.commit()
    # close
    con.close()


def return_loan(book_id, user_id, return_date, returned=True):
    # Connect
    con ,cur = connect_to_db()
    # return loan
    cur.execute(f"UPDATE Loans SET return_date='{return_date}', returned='{returned}' WHERE book_id='{book_id}' AND user_id='{user_id}'")
    con.commit()
    # close
    con.close()


def return_loans_of_deleted_book(book_id, return_date, returned=True):
    # Connect
    con ,cur = connect_to_db()
    # return all the loans of this book.
    cur.execute(f"UPDATE Loans SET return_date='{return_date}', returned='{returned}' WHERE book_id='{book_id}' AND returned='False'")
    con.commit()
    # close
    con.close()


def return_loans_of_deleted_user(user_id, return_date, returned=True):
    # Connect
    con ,cur = connect_to_db()
    # return all the loans of this user.
    cur.execute(f"UPDATE Loans SET return_date='{return_date}', returned='{returned}' WHERE user_id='{user_id}' AND returned='False'")
    con.commit()
    # close
    con.close()