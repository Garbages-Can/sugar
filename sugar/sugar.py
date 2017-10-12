from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException, NotFound


class Sugar:
    """
    Usually you create a :class:`Sugar` instance in your main module or
    in the `__init__.py` file of your package like this::

    from sugar import Sugar
    app = Flask()
    """
    secret_key = '9b7+8l35&)ldkw%5w)bg_0f=2^+%o9floh8_v)-4k0n)4^98jl'

    def __init__(self):
        self.urlmappings = dict()
        self.error_handlers = dict()
        self.url_map = Map()

    def add_url(self, url, endpoint, **options):
        options['endpoint'] = endpoint
        # there, I use all of HTTP methods.
        options.setdefault('methods',
                           ('OPTIONS', 'HEAD', 'GET', 'POST', 'PUT', 'DELETE', 'CONNECT'))
        self.url_map.add(Rule(url, endpoint))

    def dispatch_request(self, request: Request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return self.urlmappings[endpoint](**values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response, *args, **kwargs):
        return self.wsgi_app(environ, start_response)
