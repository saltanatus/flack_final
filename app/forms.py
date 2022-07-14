from flask_wtf import FlaskForm
import wtforms as wf 

class UserForm(FlaskForm):
    username = wf.StringField('Пользователь', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Пароль', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('Ок')


class PostForm(FlaskForm):
    title = wf.StringField('Загаловок', validators=[wf.validators.DataRequired()])
    content = wf.TextAreaField('Текстовая Новость', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('Ок')