from sys import argv, path

print("------------- python from import -------------")
# 因为已经导入path,argv成员，所以此处不需要加sys.path
print('path: ', path)
print("argv: ", argv)
