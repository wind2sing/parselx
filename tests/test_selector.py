from parselx import SelectorX

html = """<html>
        <body>
            <h1>Hello, ParselX!</h1>
            <ul>
                <li><a href="http://example.com">Link 1</a></li>
                <li><a href="http://scrapy.org">Link 2</a></li>
            </ul>
            <a class="latest" href="/en/latest">Link 3></a>
        </body>
        </html>"""


def test_get():
    sel = SelectorX(html)
    assert sel.g("h1::text") == "Hello, ParselX!"
    assert sel.g("_//h1/text()") == "Hello, ParselX!"


def test_getall():
    sel = SelectorX(html)
    assert sel.g("[ul li a::text]") == ["Link 1", "Link 2"]
    assert sel.g("[_//ul/li/a/text()]") == ["Link 1", "Link 2"]


def test_list_style():
    sel = SelectorX(html)
    assert (
        sel.g(["h1::text", lambda s: s.upper(), lambda s: s.split(" ")[-1]])
        == "PARSELX!"
    )


def test_vars():
    sel = SelectorX(html)
    assert sel.g("_$url", url="http://example.org") == "http://example.org"
    sel2 = SelectorX(html, vars={"url": "http://example.org"})
    assert sel2.g("_$url") == "http://example.org"
