def multiplyUtilFunction(a: float, b: float) -> float:
    return a * b


def add(a: int | float, b: int | float) -> int | float:
    """a와 b를 더한 값을 반환한다.

    >>> add(1, 2)
    3
    >>> add(-1, 1)
    0
    """
    return a + b


if __name__ == "__main__":
    print("multiplyUtilFunction test")
    assert multiplyUtilFunction(1, 2) == 2
    assert multiplyUtilFunction(0, 2) == 0
    print("ok")