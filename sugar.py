import os
import sys
from threading import local
from threading import Thread

from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import FileSystemLoader
from jinja2 import Markup
from jinja2 import escape
from werkzeug.routing import Map
from werkzeug.routing import Rule
from werkzeug.contrib.securecookie import SecureCookie


class Request():
    pass


class Response():
    pass


class _RequestGlobals():
    pass


class Sugar():
    pass
