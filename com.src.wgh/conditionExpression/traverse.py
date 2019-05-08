"""
break 语句可以跳出 for 和 while 的循环体。
如果从 for 或 while 循环中终止，任何对应的循环 else 块将不执行

continue 语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环
"""
# import sys

sites = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
print("sites: ", sites)
print("使用range遍历：")
for i in range(len(sites)):
    print(i, sites[i])

print("使用iter遍历：")
it = iter(sites)
for x in it:
    print(x, end="\n")

print("使用next()函数遍历：")
iters = iter(sites)

while True:
    try:
        print(next(iters))
    except StopIteration:
        # sys.exit()
        break

print("循环匹配")
for site in sites:
    if site == "Runoob":
        print("菜鸟教程")
        break
    print("循环数据：", site)
else:
    print("没有循环数据！")
print("完成循环！")

'''
Python pass是空语句，是为了保持程序结构的完整性
pass 不做任何事情，一般用做占位语句
'''
