"""
Python 成员运算符

    and: 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
    or: 布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。
    not: 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
"""


a = 10
b = 20
c = -10
d = False
e = True
f = 0
g = 1

print(a and b)
print(c and b)
print(d and b)
print(e and b)
print(f and b)
print(g and b)

if a and b:
    print("1: 变量a 和 b 都为 true")
else:
    print("1: 变量a 和 b 有一个不为为 true")


if c and b:
    print("2: 变量a 和 b 都为 true")
else:
    print("2: 变量a 和 b 有一个不为为 true")

if f and b:
    print("3: 变量a 和 b 都为 true")
else:
    print("3: 变量a 和 b 有一个不为为 true")

"""
Python 身份运算符

    is: is 是判断两个标识符是不是引用自一个对象
    is not: is 是判断两个标识符是不是引用自不同对象
"""

# id() 函数用于获取对象内存地址
a = 20
b = 20

print(id(a))
print(id(b))

if a is b:
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if id(a) == id(b):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if a is b:
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if a is not b:
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")

'''
is 与 == 区别：

is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''


