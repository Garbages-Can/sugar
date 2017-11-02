from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from ._context import _request_ctx_stack
from ._context import current_app
from ._context import session
from ._context import request

from .sugar import Sugar

__version__ = '0.1.0'


def url_for(endpoint, **values):
    """Generates a URL to the given endpoint with the method provided.

    :param endpoint: the endpoint of the URL (name of the function)
    :param values: the variable arguments of the URL rule
    """
    return _request_ctx_stack.top.url_adapter.build(endpoint, values)
