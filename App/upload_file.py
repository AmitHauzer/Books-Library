import os
from flask import flash, request
from werkzeug.utils import secure_filename
from colorama import Fore

# UPLOAD_FOLDER = r'.\App\static\books_images'
UPLOAD_FOLDER = r'./App/static/books_images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'picture' not in request.files:
            flash('No file part')
            # return redirect(request.url)
        file = request.files['picture']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            # return redirect(url_for('download_file', name=filename))
    else:
        print('its not POST method')


def delete_file(book_picture):
    file_path = UPLOAD_FOLDER+'/'+book_picture
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print("File has been deleted - Done.")
        else:
            print("File does not exist")
    except Exception as ex:
        print(f"{Fore.RED} {ex} {Fore.RESET}")








# def check_a_file():









# @app.route('/uploads/<name>')
# def download_file(name):
    # return send_from_directory(current_app.config["UPLOAD_FOLDER"], name)


# app.run(debug=True)