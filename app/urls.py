from . import views
from . import app

# urls for posts

app.add_url_rule('/', view_func=views.index, methods=['GET'], endpoint='index')
app.add_url_rule('/post/add', view_func=views.post_add, methods=['GET', 'POST'], endpoint='post_add')

# urls for user

app.add_url_rule('/register', view_func=views.register, methods=['GET', 'POST'], endpoint='register')
app.add_url_rule('/login', view_func=views.login, methods=['GET', 'POST'], endpoint='login')