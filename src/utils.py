def multiplyUtilFunction(a, b):
    return a * b


if __name__ == "__main__":
    print("multiplyUtilFunction test")
    assert multiplyUtilFunction(1, 2) == 2
    assert multiplyUtilFunction(0, 2) == 0
    print("ok")
