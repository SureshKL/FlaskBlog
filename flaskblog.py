import datetime

from flask import Flask, render_template, url_for, flash, redirect


from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config[
    'SECRET_KEY'] = 'c20c6209d6f9eb67fde7ddb1e007ac6c72a0bae8e7bffdaca471b391d6c5fe80'
# Secret key can be obtained using secrets module

posts = [
    {
        'author': 'Suresh K L',
        'title': 'Post 1',
        'content': 'First post',
        'date_posted': datetime.datetime.now(),
    },
    {
        'author': 'Vany',
        'title': 'Post 2',
        'content': 'Second post',
        'date_posted': datetime.datetime.now(),
    },

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.data.email == 'suresh1591@gmail.com' and form.data.password == 'pass':
            flash('You have been logged in!!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
