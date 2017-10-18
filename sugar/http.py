from werkzeug.wrappers import Request as RequestBase
from werkzeug.wrappers import Response as ResponseBase


class Request(RequestBase):
    """
    The request object used by default in sugar.
    Remembers the matched endpoint and view arguments.
    """

    def __init__(self, environ):
        RequestBase.__init__(self, environ)
        self.endpoint = None
        self.view_args = None


class Response(ResponseBase):
    """
    The response object that is used by default in sugar.  Works like the
    response object from Werkzeug but is set to have a HTML mimetype by
    default.
    """
    default_mimetype = 'text/html'
