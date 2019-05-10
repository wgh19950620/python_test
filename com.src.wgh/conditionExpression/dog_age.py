age = int(input("请输入你家狗狗的年龄："))
print("")
if age < 0:
    print("狗狗年龄怎么能负数呢！")
elif age == 1:
    print("相当于人14岁")
elif age == 2:
    print("相当于人22岁")
elif age > 2:
    person = 22 + (age - 2) * 5
    print("对应人年龄：", person)
else:
    print("Good Bye!")
input("点击 enter 键退出")
