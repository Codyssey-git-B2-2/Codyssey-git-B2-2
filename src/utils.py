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

def divide(a: int | float, b: int | float) -> float:
    """a를 b로 나눈 값을 반환한다. 0으로 나눌 경우 ZeroDivisionError를 발생시킨다.

    >>> divide(6, 2)
    3.0
    >>> divide(5, 2)
    2.5
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


if __name__ == "__main__":
    print("[RUN] utils test suite")
    # multiply & divide 테스트를 한 블록으로 묶음
    assert multiply(1, 2) == 2 and multiply(0, 2) == 0
    assert divide(6, 2) == 3.0
    assert divide(5, 2) == 2.5
    
    # add & subtract 테스트
    assert add(1, 2) == 3 and add(-1, 1) == 0
    assert subtract(3, 1) == 2 and subtract(1, 3) == -2
    print("[PASS] all tests passed successfully")
