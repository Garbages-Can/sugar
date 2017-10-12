from .sugar import Sugar

import os

base_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(base_dir, 'templates')
static_path = os.path.join(base_dir, 'static')

from jinja2 import Environment, FileSystemLoader
from werkzeug.wrappers import Request, Response

_jinja_env = Environment(loader=FileSystemLoader, autoescape=True)


def render_template(template_name: str, **context) -> Response:
    template = _jinja_env.get_template(template_name)
    return Response(template.render(**context), mimetype='text/html')
