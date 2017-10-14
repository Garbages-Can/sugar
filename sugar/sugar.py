import os
from numbers import Integral

from jinja2 import Environment, FileSystemLoader
from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.routing import Map, Rule

# base_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_path = os.path.join(base_dir, 'templates')
static_path = os.path.join(base_dir, 'static')

jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)


def render_template(template_name, **context):
    template = jinja_env.get_template(template_name)
    return Response(template.render(context), mimetype='text/html')


class Sugar:
    """
        Usually you create a :class:`Sugar` instance in your main module or
        in the `__init__.py` file of your package like this::

        from sugar import Sugar
        sugar = Sugar()
    """

    secret_key = '9b7+8l35&)ldkw%5w)bg_0f=2^+%o9floh8_v)-4k0n)4^98jl'

    def __init__(self):
        #: the debug flag.  Set this to `True` to enable debugging of
        #: the application.  In debug mode the debugger will kick in
        #: when an unhandled exception ocurrs and the integrated server
        #: will automatically reload the application if changes in the
        #: code are detected.
        self.debug = False

        #: a dictionary of all view functions registered.  The keys will
        #: be function names which are also used to generate URLs and
        #: the values are the function objects themselves.
        #: to register a view function, use the :meth:`url_mapping`
        #: decorator.
        self.url_mappings = {}

        #: a dictionary of all registered error handlers.  The key is
        #: be the error code as integer, the value the function that
        #: should handle that error.
        #: To register a error handler, use the :meth:`error_mapping`
        #: decorator.
        self.error_mappings = {}

        self.url_map = Map()
        self.func_name_of_404 = None

    def add_url(self, url, endpoint, **options):
        options['endpoint'] = endpoint
        options.setdefault('methods', ('GET', 'POST'))
        self.url_map.add(Rule(url, **options))

    def url_mapping(self, url: str, **options):
        """
        A decorator that is used to register a view function for a given URL rule.
        for example:
        @sugar.url_mapping('/')
        def index():
            return render_template('index.html')

        @sugar.url_mapping('/<username>')
        def user(username):
            return render_template('user.html', username=username)
        :param url: endpoint
        """

        def decorator(func):
            self.add_url(url, func.__name__, **options)
            self.url_mappings[func.__name__] = func
            return func

        return decorator

    def error_mapping(self, code: Integral):
        """
        A decorator that is used to register a function give a given error code.
        for example:
        @sugar.error_mapping(404)
        def page_not_found():
            return render_template('404.html')
        """

        def decorator(func):
            self.add_url('/' + str(code), func.__name__)
            self.error_mappings[func.__name__] = func
            self.func_name_of_404 = func.__name__
            return func

        return decorator

    def run(self, hostname='localhost', port=1129, **options):
        """
        Runs the application on a local development server.
        If the attribute
            :`debug` flag is set the server will automatically reload
        for code changes and show a debugger in case an exception happened.
            :param host: the hostname to listen on.
            :param port: the port of the webserver
            :param options: the options to be forwarded to the underlying Werkzeug server.
        """
        from werkzeug.serving import run_simple
        if 'debug' in options:
            self.debug = options.pop('debug')
        run_simple(hostname, port, self, **options)

    # deal with requests
    def dispatch_request(self, request: Request):
        # This function is the core of the whole framework.
        # Because scheduling requests from all users(browsers).
        adapter = self.url_map.bind_to_environ(request.environ)
        endpoint, values = str(), {}
        try:
            endpoint, values = adapter.match()
            return self.url_mappings[endpoint](**values)
        except HTTPException:
            return self.error_mappings[self.func_name_of_404](**values)

    def wsgi_app(self, environ, start_response):
        """The actual WSGI application.  This is not implemented in
        `__call__` so that middlewares can be applied:

            app.wsgi_app = MyMiddleware(app.wsgi_app)

        :param environ: a WSGI environment
        :param start_response: a callable accepting a status code,
                               a list of headers and an optional
                               exception context to start the response
        """
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response, *args, **kwargs):
        return self.wsgi_app(environ, start_response)
