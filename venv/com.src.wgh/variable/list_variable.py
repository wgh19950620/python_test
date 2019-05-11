"""
注意：
    1、List写在方括号之间，元素用逗号隔开。
    2、和字符串一样，list可以被索引和切片。
    3、List可以使用+操作符进行拼接。
    4、List中的元素是可以改变的。
"""
list_test = ['hello', 786, 2.23, 'python', 70.2]
tiny_list = [123, 'python']

print("list_test: ", list_test)  # 输出完整列表
print(list_test[0])  # 输出列表第一个元素
print(list_test[1:3])  # 从第二个开始输出到第三个元素
print(list_test[2:])  # 输出从第三个元素开始的所有元素
print(tiny_list * 2)  # 输出两次列表
print("list_test + tiny_list: ", list_test + tiny_list)  # 连接列表

print("嵌套列表")
lists = [list_test, tiny_list]
print("lists: ", lists)

'''
Python 列表截取可以接收第三个参数，参数作用是截取的步长，
以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串
'''
print("list 截取步长")
letters = ["a", "b", "c", "d", "e", "f"]
print("letters: ", letters)
print(letters[1:4])
# 1-4 为b,c,d,e不包含e, 步长为从b开始到d的距离即d
print(letters[1:4:2])

print("list 更新数据")
print("letters[2]: " + letters[2])
letters[2] = "g"
print("letters[2]: " + letters[2])

print("删除第三个元素")
del letters[2]
print("letters: ", letters)

print("迭代")
for x in letters:
    print(x, end="\n")

print("返回列表最大值")
print(max(letters))

print("在末尾添加新的对象")
letters.append("g")
print("letters: ", letters)

print("插入对象")
letters.insert(2, "c")
print("letters: ", letters)
print(letters.pop(), letters)

