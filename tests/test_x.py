from parselx import SelectorX, x

html = """<html>
        <body>
            <h1>Hello, ParselX!</h1>
            <h2>   Blank   <h2>
            <h3> 2000 <h3>
            <ul>
                <li><a href="http://example.com">Link 1</a></li>
                <li><a href="http://scrapy.org">Link 2</a></li>
            </ul>
        </body>
        </html>"""


def test_filters():
    sel = SelectorX(html)
    assert sel.g(["h1::text", "reverse"]) == "!XlesraP ,olleH"
    assert sel.g(["h2::text"]) == "   Blank   "
    assert sel.g(["h2::text", "strip"]) == "Blank"


def test_methods():
    sel = SelectorX(html)
    assert sel.g(["h2::text", x.strip()]) == "Blank"
    assert sel.g(["[a::text]", x.first()]) == "Link 1"


def test_use():
    sel = SelectorX(html)
    x.use({"cut": lambda s, length: s[: int(length)]})
    assert sel.g(["h1::text", "cut:5"]) == "Hello"


def test_register():
    sel = SelectorX(html)

    @x.register("to_int")
    def _(val):
        return int(val)

    assert sel.g(["h3::text", "to_int"]) == 2000

