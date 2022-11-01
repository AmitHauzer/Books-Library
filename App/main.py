
from flask import Flask, redirect, url_for
from App.admin import admin_bp
from App.login import login_bp
from App.home import home_bp
from App.loans import loan_bp
from App.settings import settings_bp


app = Flask(__name__)
app.secret_key = 'afaw#@$56ty$%TGtrhE%^U%YTHDFGr5ytergyuk7*I&*IUTYghfghr6yr5ty45Ytr6yr'
app.register_blueprint(admin_bp)
app.register_blueprint(login_bp)
app.register_blueprint(home_bp)
app.register_blueprint(loan_bp)
app.register_blueprint(settings_bp)


@app.route("/")
def main():
    return redirect(url_for('home.home'))


if __name__ == "__main__":
    app.run(debug= True)

