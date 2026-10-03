def multiplyUtilFunction(a, b):
    return a * b


if __name__ == "__main__":
    print("multiply test")
    assert multiply(1, 2) == 2
    assert multiply(0, 2) == 0
    print("ok")
