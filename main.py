def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, 3) == 4
    assert add(1, 4) == 5

if __name__ == '__main__':
    test_add()
    print('All tests passed.')