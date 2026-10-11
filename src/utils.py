def multiply(a, b):
    return a * b

def add(a: int | float, b: int | float) -> int | float:
    """a와 b를 더한 값을 반환한다.

    >>> add(1, 2)
    3
    >>> add(-1, 1)
    0
    """
    return a + b

def subtract(a: int | float, b: int | float) -> int | float:
    """a에서 b를 뺀 값을 반환한다.

    >>> subtract(3, 1)
    2
    >>> subtract(1, 3)
    -2
    """
    return a - b


if __name__ == "__main__":
    print("multiply test")
    assert multiply(1, 2) == 2
    assert multiply(0, 2) == 0
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert subtract(3, 1) == 2
    assert subtract(1, 3) == -2
    print("ok")
