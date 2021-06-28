from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = ''

posts = [
  {
    'author': 'Cory Bolls',
    'title': 'Blog Post Food',
    'content': 'First post content',
    'date_posted': 'April 20, 2021'
  },
  {
    'author': 'Papa Graziani',
    'title': 'How to make lamps',
    'content': 'You need love and glue',
    'date_posted': 'March 20, 2021'
  },
  {
    'author': 'Olivia Graziani',
    'title': 'How to not eat lunch',
    'content': 'Watch cocomelon',
    'date_posted': 'April 27, 2021'
  }
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