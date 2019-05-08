"""
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这些语句内定义的变量，外部也可以访问

Python的作用域一共有4种，分别是：

L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内置作用域（内置函数所在模块的范围）
"""

g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中
    print(o_count)

    def inner():
        i_count = 2  # 局部作用域
        return i_count


outer()

'''
内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。
在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量:
'''
import builtins

print(dir(builtins))
