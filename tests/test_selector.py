from parselx import SelectorX
import pytest

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
    assert sel.g("h1") == "Hello, ParselX!"
    assert sel.g("body > a@href") == "/en/latest"
    assert sel.g("h1@html") == "<h1>Hello, ParselX!</h1>"
    assert sel.g("_//h1/text()") == "Hello, ParselX!"


def test_getall():
    sel = SelectorX(html)
    assert sel.g("[ul li a]") == ["Link 1", "Link 2"]
    assert sel.g("[_//ul/li/a/text()]") == ["Link 1", "Link 2"]


def test_list_style():
    sel = SelectorX(html)
    assert sel.g(["h1", lambda s: s.upper(), lambda s: s.split(" ")[-1]]) == "PARSELX!"


def test_callable_rule():
    sel = SelectorX(html)
    assert sel.g(lambda: "hello") == "hello"


def test_xpath_vars():
    sel = SelectorX(html)
    assert sel.g("_$url", url="http://example.org") == "http://example.org"
    sel2 = SelectorX(html, vars={"url": "http://example.org"})
    assert sel2.g("_$url") == "http://example.org"
    assert (
        sel2.xpath(
            "$url", namespaces={"i": "http://schema.intuit.com/finance/v3"}
        ).get()
        == "http://example.org"
    )


def test_selectorlistX():
    sel = SelectorX(html, vars={"url": "http://example.org"})
    sels = sel.css("li a")
    r = sels.g("[@text]")
    assert r == ["Link 1", "Link 2"]
    assert sels.g("_$url") == "http://example.org"


def test_query_error():
    sel = SelectorX(html)
    with pytest.raises(TypeError):
        sel.g(1)
    with pytest.raises(TypeError):
        sel.g(["[a]", 1])


def test_xpath_error():
    sel = SelectorX(html)
    with pytest.raises(ValueError):
        sel.g("_///")
