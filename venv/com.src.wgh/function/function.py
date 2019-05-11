"""
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

Python 定义函数使用 def 关键字，一般格式如下：
    def 函数名（参数列表):
        函数体
"""


# 计算面积函数
def area(width, length):
    return width * length


w = 4
h = 5
print("width =", w, "height =", h, " area =", area(w, h))

'''
函数参数的使用不需要使用制定顺序
'''


def printInfo(name, age=35):
    print("name: ", name)
    print("age: ", age)
    return


printInfo(age=50, name="zhangsan")

printInfo(name="lisi")


'''
不定长参数：
    def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
   
   加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
'''


def printTuple(arg1, *vartuple):
    print("arg1: ", arg1)
    print("vartuple: ", vartuple)


printTuple(70, 80, 90)
print("-------------------")
printTuple(70)


