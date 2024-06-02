from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class Registracion(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Эл. почта', validators=[DataRequired(), Email()])
    password = PasswordField('Введите пароль', validators=[DataRequired(), Length(min=7)])
    repeat_password = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])