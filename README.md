
                    // Sugar //

            A minimal web framework by Python.

        Sugar tastes sweet.You feel bored when you repeat
        the CGI script and write the database code repeatedly.
        No one wants to focus on how to output Content-Type
        and to shut down the database after all operations
        have been done.So, you need a spoon of sugar liberated
        from the saccharification, repeated work.



## Features
- extensible
- URL mapping
- error handling (404,500)
- template rendering
- HttpReqeust, HttpResponse
- context
- cache (thread safty)

## Document

[https://ltoddy.github.io/sugar/docs/](https://ltoddy.github.io/sugar/docs/)


## Usage:

> python3 setup.py install

```python
from sugar import Sugar


sugar = Sugar(__name__)


@sugar.url_mapping('/')
def index():
    return sugar.render_template('index.html')

if __name__ == '__main__':
    sugar.run(debug=True)

```