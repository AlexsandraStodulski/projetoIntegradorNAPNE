from flask import Flask, render_template, request, redirect, url_for
import Usuario
import flask_login

app = Flask(__name__)
app.secret_key = 'super secret string'  # Change this!

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

users = {'a@a.com': {'password': '123'}}

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = Usuario.Usuario()
    user.id = email
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        if request.form['password'] == users[email]['password']:
            user = Usuario.Usuario()
            user.id = email
            flask_login.login_user(user)
        return redirect(url_for('protected'))

    return render_template('pages/login.html')


@app.route('/')
@flask_login.login_required
def index():
    return render_template('pages/index.html')

@app.route('/formulario')
def formulario():
    return render_template('pages/formulario.html')

@app.route('/ficha')
def ficha():
    return render_template('pages/ficha.html')


@app.route('/protected')
@flask_login.login_required
def protected():
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
