
from flask import flash, render_template, request, redirect, Blueprint, session, url_for
from App.login import login_required
from App.Data.data import get_an_object_from_db_with_id, add_loan_in_db, return_loan, user_loans
from datetime import date, timedelta

loan_bp = Blueprint('loan', __name__, url_prefix='/loan')



@loan_bp.route('/', methods=['GET', 'POST'])
@login_required
def loan_a_book():
    # the relevant book
    book_id = request.args.get('id')
    book = get_an_object_from_db_with_id(id_pk = book_id)
    # loan date
    today = date.today()
    
    if request.method == 'POST':
        # return date
        return_date = convert_str_to_date(date_str= request.form.get('return_date'))
        # days for loan
        diff = return_date - today
        print(f"{return_date} - {today} = {diff.days}")
        # ths relevant user
        user_id = session.get('user_id')
        # add loan in DB
        add_loan_in_db(loan_date= today, return_date= return_date, book_id= book_id, user_id= user_id, returned=False)
        flash(f"You loaned the book {book['Book']}")
        return redirect(url_for('home.home'))

    dates = {'today': today, 'two months': today + timedelta(days=60)}
    return render_template('loan_form.html',data= book, dates= dates)



@loan_bp.route('/returnbook')
@login_required
def return_a_loan():
    book_id = request.args.get('id')
    user_id = session.get('user_id')
    return_date = date.today()
    return_loan(book_id= book_id, user_id= user_id, return_date= return_date, returned=True)
    flash('The book has been returned', category='message')
    return redirect(url_for('home.home'))


def check_the_user_loans():
    books_id= []
    if session:
        user_id = session['user_id']
        all_user_loans = user_loans(user_id)
        for loan in all_user_loans:
            if check_the_loan_date(loan= loan):
                continue
            books_id.append(loan['book_id'])
        return books_id, all_user_loans
    else:
        return books_id


def check_the_loan_date(loan):
    today = date.today()
    return_date = convert_str_to_date(date_str= loan['return_date'])
    if today >= return_date:
        return_loan(book_id= loan['book_id'], user_id= loan['user_id'], return_date= today, returned=True)
        return True
    else:
        return False
    

def convert_str_to_date(date_str):
    converter = date_str.split('-')
    converter = date(int(converter[0]), int(converter[1]), int(converter[2]))
    return converter