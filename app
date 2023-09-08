from flask import Flask, render_template, request, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'u-will-never-guess'
db = SQLAlchemy(app)
migrate = Migrate(app, db)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))


    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return redirect('/news')
        else:
            flash('Неправильне ім\'я користувача або пароль', 'error')

    return render_template('login.html')

@app.route('/news')
def news():
    def get_news():
        api_key = "c792ecc9a9764f9caee4fd756ecb1318"
        url = 'https://newsapi.org/v2/top-headlines'

        params = {
            'apiKey': api_key,
            'country': 'ua',
            'language': 'uk',
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            news_data = response.json()
            articles = news_data.get('articles', [])
            return articles
        else:
            print("Помилка запиту:", response.status_code)
            return []

    news = get_news()
    return render_template('news.html', news=news)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Користувач з таким іменем вже існує', 'error')
        else:
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Реєстрація успішно завершена', 'success')
            return redirect('/news')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
