data = "hello world"

message = "hello python"

total_one = data + \
            ", " + \
            message

total_second = ["data" +
                "data"]
print("total_second: " + total_one)

print("data: " + data)  # 输出字符串
print("data: " + data[0:-1])  # 输出第一个到倒数第二个的所有字符
print("data: " + data[0])  # 输出字符串第一个字符
print("-----------------------")
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
print("data: " + data[2:5], end=" ")  # 输出从第三个开始到第五个的字符
print("data: " + data[2:])  # 输出从第三个开始的后的所有字符
print("data: " + data * 2)  # 输出字符串两次
print("data: " + data + '你好')  # 连接字符串

# Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串
total_thread = r"hello world, hello python\n"
print("total_thread: " + total_thread)

'''
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {}
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
'''
if True:
    print(total_one)
else:
    print(message)
