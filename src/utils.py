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


def divide(a: int | float, b: int | float) -> float:
    """a를 b로 나눈 값을 반환한다."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b


if __name__ == "__main__":
    print("multiply test")
    assert multiply(1, 2) == 2
    assert multiply(0, 2) == 0
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert divide(4, 2) == 2.0
    print("ok")