from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Marius Schaefer',
        'title': 'Test',
        'content': 'Test',
        'date_posted': 'January 21st, 2020'
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)