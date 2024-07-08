from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = '6d0d6a76c0e1522467f9cc1681db0a5972bd1c30a03832d1af4b71f381698f84'


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('hello', name = session["username"]))                         #f'Привет, {session["username"]}'
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Страница входа')


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        session.pop('username', None)
        return redirect(url_for('index'))
    return render_template("hello.html", name = session["username"], title = 'Страница приветствия')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
