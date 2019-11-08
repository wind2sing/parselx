parselx
=======


Enhanced version of `parsel <https://parsel.readthedocs.io/en/latest/>`_, extracting data from HTML and XML using complex rules.


Features
--------

* Magic `g` method, extract items by complex rules
* Apply filters to a value, appended in rule
* `x` instance: many helper methods and filters

Plus all the standard features of `parsel`


.. code-block::

    >>> from parselx import SelectorX
    >>> sel = SelectorX("""<html>
            <body>
                <h1>Hello, Parselx!</h1>
                <ul>
                    <li><a href="http://example.com">Link 1</a></li>
                    <li><a href="http://scrapy.org">Link 2</a></li>
                </ul>
            </body>
            </html>""")
    >>>
    >>> sel.g('h1::text')
    'Hello, Parselx!'
    >>> sel.g('[ul li a::text]')
    ['Link 1', 'Link 2']
    >>> sel.g({'title':['h1::text', lambda s: s.upper()], 'links':'[a::attr(href)]'})
    {'title': 'HELLO, PARSELX!', 'links': ['http://example.com', 'http://scrapy.org']}



Installation
------------

To install, simply use `pipenv <http://pipenv.org/>`_ (or pip):

.. code-block:: bash

   $ pipenv install parselx
