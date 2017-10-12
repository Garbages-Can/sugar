from sugar import Sugar
from sugar import render_template

app = Sugar()


@app.url_mapping('/')
def index():
    return render_template('index.html')


@app.url_mapping('/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)

    # /home/me/github/Sugar/sugar
    # /home/me/github/Sugar/sugar/templates
    # /home/me/github/Sugar/sugar/static
