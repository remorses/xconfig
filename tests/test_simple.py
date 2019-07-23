
from xconfig import Config


def test_simple():
    c = Config('./test.yaml')
    c.write('tests.test.cosa', 69)
    c.write('tests.test.altro', 69)
    print()
    print(c)
    assert True