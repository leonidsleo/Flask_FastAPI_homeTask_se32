from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect

from form import Registracion
from models import db, User

import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex()

csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Привет'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Создана база')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = Registracion()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        new_user = User(name=name, surname=surname, email=email, password=password)
        new_user.generet_password(password)
        db.session.add(new_user)
        db.session.commit()
        return "ВЫ ЗАРЕГИСТРИРОВАНЫ"

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)