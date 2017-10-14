from sugar import Sugar
from sugar import render_template

sugar = Sugar()


@sugar.url_mapping('/')
def index():
    return render_template('index.html')


@sugar.url_mapping('/<name>')
def user(name):
    return render_template('user.html', name=name)


@sugar.error_mapping(404)
def page_not_found():
    return render_template('404.html')


if __name__ == '__main__':
    sugar.run(debug=True)
