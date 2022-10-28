from flask import render_template, request, Blueprint
from App.Data.data import get_all_books_from_db, get_a_book_from_db, search_by_book_name, user_loans
from App.loans import check_the_user_loans
from App.login import login_required

home_bp = Blueprint('home', __name__, url_prefix='/home')



@home_bp.route("/")
def home():
    books = get_all_books_from_db()
    loans_of_books = check_the_user_loans()
    return render_template('home.html', data= books, loans= loans_of_books)


@home_bp.route("/book")
@login_required
def book():
    id_pk = request.args.get('id')
    book = get_a_book_from_db(id_pk = id_pk)
    loans_of_books = check_the_user_loans()
    return render_template('book.html', data= book, loans= loans_of_books)


@home_bp.route('/search')
def search_a_book():
    book_name = request.args.get('search')
    results = search_by_book_name(book_name= book_name)
    loans_of_books = check_the_user_loans()
    return render_template('home.html', data= results, loans= loans_of_books)


@home_bp.route('/loanslist')
@login_required
def loans_list():
    loans_books = []
    loans_of_the_user = check_the_user_loans()
    for book_id in loans_of_the_user[0]:
        book = get_a_book_from_db(id_pk = book_id)
        loans_books.append(book)
    return render_template('home.html', data= loans_books, loans= loans_of_the_user) 

