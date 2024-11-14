from flask import render_template, request, redirect, url_for
from . import app

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        return redirect(url_for('usuario', user=username))
    return render_template('login.html')

@app.route('/usuario/<user>')
def usuario(user):
    return render_template('usuario.html', user=user)