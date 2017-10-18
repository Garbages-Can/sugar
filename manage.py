from sugar import Sugar

sugar = Sugar(__name__)


@sugar.url_mapping('/')
def index():
    return sugar.render_template('index.html')


@sugar.url_mapping('/<name>')
def user(name):
    return sugar.render_template('user.html', name=name)


@sugar.error_mapping(404)
def page_not_found():
    return sugar.render_template('404.html')


if __name__ == '__main__':
    sugar.run(debug=True)
