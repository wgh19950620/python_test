def a():
    """这是文档字符串"""
    pass


print(a.__doc__)

b = 1
while b < 7:
    if b % 2 == 0:
        print(b, "is even")
    else:
        print(b, "is odd")
    b += 1
