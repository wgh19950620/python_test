"""
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
"""

dic_test = {'one': "1 - 菜鸟教程", 2: "2 - 菜鸟工具"}

tiny_dict = {'name': 'python', 'code': 1, 'site': 'www.python.com'}

print("dic_test['one']: ", dic_test['one'])  # 输出键为 'one' 的值
print(dic_test[2])  # 输出键为 2 的值
print("tiny_dict: ", tiny_dict)  # 输出完整的字典
print(tiny_dict.keys())  # 输出所有键
print("type(tiny_dict.keys()): ", type(tiny_dict.keys()))
print(tiny_dict.values())  # 输出所有值

'''
构造函数 dict() 可以直接从键值对序列中构建字典如下：
'''
dic_one = dict([('baidu', 1), ('Google', 2), ('Taobao', 3)])
print("dic_one: ", dic_one)

dic_second = {x: x**2 for x in (2, 4, 6)}
print("dic_second: ", dic_second)
print(dic_second[2])

dic_thread = dict(baidu=1, Google=2, Taobao=3)
print("dic_thread: ", dic_thread)

print("对dic_thread数据进行操作")
dic_thread["baidu"] = 4
dic_thread["Tianmao"] = 5

print("dict_thread: ", dic_thread)

del dic_thread["baidu"]
print("dict_thread: ", dic_thread)

'''
另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。

注意：
    1、字典是一种映射类型，它的元素是键值对。
    2、字典的关键字必须为不可变类型，且不能重复。
    3、创建空字典使用 { }。
'''

