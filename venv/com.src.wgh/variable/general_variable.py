"""
Python3 中有六个标准的数据类型：
    Number（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Set（集合）
    Dictionary（字典）

Python3 的六个标准数据类型中：
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
"""

a = b = c = 1
print(a, b, c)

a, b, c, d = 1, 2.0, "python", True
print(a, b, c)

# 除法，得到一个浮点数
print("5 / 2: ")
print(5 / 2)
# 除法，得到一个整数
print("5 // 2: ")
print(5 // 2)

'''
Python3 Number 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
内置的 type() 函数可以用来查询变量所指的对象类型。

注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
    到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
'''
print(type(a), type(b), type(c), type(d))

print(b + d)

print(isinstance(a, int))

'''
isinstance 和 type 的区别在于：
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。
'''


class A_Test:
    pass


class B_Test(A_Test):
    pass


print(isinstance(B_Test(), A_Test))
print(A_Test == B_Test)
print("type(A_Test()): ", type(A_Test()))
print("type(B_Test()): ", type(B_Test()))
print(type(B_Test) == type(A_Test))
