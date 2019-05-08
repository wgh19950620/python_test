"""
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
元组中的元素类型也可以不相同

元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取
元组元素不可被修改
虽然tuple的元素不可改变，但其可以包含可变对象，如list列表
"""

tuple_test = ('hello', 786, 2.23, 'python', 70.2)
tiny_tuple = (123, 'python')

print("tuple_test: ")
print(tuple_test)  # 输出完整元组
print(tuple_test[0])  # 输出元组的第一个元素
print(tuple_test[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple_test[2:])  # 输出从第三个元素开始的所有元素
print(tiny_tuple * 2)  # 输出两次元组
print("tuple_test + tiny_tuple: ")
print(tuple_test + tiny_tuple)  # 连接元组

''' 
包含 0 个或 1 个元素的元组比较特殊，有额外的语法规则：
元组中只包含一个元素是，需要在元素后面添加逗号，否则会被当作运算符使用
'''
tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
print(type(tup2))


'''
string、list 和 tuple 都属于 sequence（序列）。

注意：
    1、与字符串一样，元组的元素不能修改。
    2、元组也可以被索引和切片，方法一样。
    3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
    4、元组也可以使用+操作符进行拼接。
'''

