"""
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""

student = {"Tom", "Mary", "Tom", "Jack", "Rose"}
# 输出集合，重复的元素被自动去掉，且无序
print(student)

if 'Rose' in student:
    print("Rose 在集合中")
else:
    print("Rose 不在集合中")

# set可以进行集合运算

a = set('abracadabra')
b = set('alacazam')

print("a: ", a)
print("b: ", b)
print(a - b)  # a 和 b 的差集,集合a中包含而集合b中不包含的元素
print(a | b)  # a 和 b 的并集，集合a与集合b包含的所有元素
print(a & b)  # a 和 b 的交集，集合a与集合b都包含的元素
print(a ^ b)  # a 和 b 中不同时存在的元素，不同时包含于a和b中的元素

c = {x for x in 'abracadabra' if x not in 'abc'}
print("c: ", c)

'''
添加元素：
    s.add(x)
    s.update(x)
'''

set_test = {"baidu", "Google", "Taobao"}
print("set_test: ", set_test)
set_test.add("facebook")
print("set_test: ", set_test)

'''
移出元素：
    s.remove(x)
    s.discard(x)
随机删除元素，并返回删除的元素：
    s.pop()
'''
tiny_set = set(("baidu", "Google", "Taobao"))
print("tiny_set: ", tiny_set)
tiny_set.remove("baidu")
print("tiny_set: ", tiny_set)
tiny_set.discard("Taobao")
print("tiny_set: ", tiny_set)

print("a.pop(): ", a.pop())


