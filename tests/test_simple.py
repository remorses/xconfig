
from xconfig import Config, AsyncConfig
import pytest

def test_simple():
    c = Config('./test.yaml')
    c.delete()
    c.write('tests.test.cosa', 69)
    c.write('tests.test.altro', 69)
    for i in range(5):
        c.push('tests.test.array', i)
    print()
    print(c)
    assert True

@pytest.mark.asyncio
async def test_async():
    c = await AsyncConfig('./test.yaml')
    await c.delete()
    await c.write('tests.test.cosa', 69)
    await c.write('tests.test.altro', 69)
    for i in range(5):
        await c.push('tests.test.array', i)
    print()
    print(c)
    assert True