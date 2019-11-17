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
    >>> sel.g('h1')
    'Hello, Parselx!'
    >>> sel.g('h1 | reverse')
    '!xlesraP ,olleH'
    >>> sel.g('[ul li a]')
    ['Link 1', 'Link 2']
    >>> sel.g({'title':['h1', lambda s: s.upper()], 'links':'[a @href]'})
    {'title': 'HELLO, PARSELX!', 'links': ['http://example.com', 'http://scrapy.org']}
    >>> sel.g('[ul li a @href| map:slice,7,-4]')
    ['example', 'scrapy']




Installation
------------


.. code-block:: bash

   $ pip install parselx
