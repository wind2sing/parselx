from parselx.utils import parse_query, partial


def test_parse_query():
    query = " h1 "
    assert parse_query(query) == {
        "lang": "css",
        "meth": "get",
        "query": "h1",
        "filters": [],
    }
    query = " [h1 ]"
    assert parse_query(query) == {
        "lang": "css",
        "meth": "getall",
        "query": "h1",
        "filters": [],
    }
    query = " _//h1/text() "
    assert parse_query(query) == {
        "lang": "xpath",
        "meth": "get",
        "query": "//h1/text()",
        "filters": [],
    }


def test_partial():
    def cal(a, b, c):
        return a * (b + c)

    cal2 = partial(cal, 2, 3)
    assert cal2(4) == 14

    cal3 = partial(cal, 2, 3, new_args_before=True)
    assert cal3(4) == 20
