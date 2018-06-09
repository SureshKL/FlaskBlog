import datetime

from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
