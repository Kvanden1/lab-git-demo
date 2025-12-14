from hello import hello, add

def test_hello():
    assert hello() == "Hello World"

def test_add():
    assert add(2, 3) == 5
