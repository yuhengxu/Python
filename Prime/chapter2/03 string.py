#对字符串的操作

#使用方法修改字符串的大小写
print("-------将字符串首字母大写---------")
name = "ada lovelace"
print(name.title())
print("----------------")

#将字符串全部改写为大写或小写
print("------将字符串全部改为大写或小写----------")
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
print("----------------")

#合并拼接字符串
print("-------合并拼接字符串---------")
first_name = "ada"
last_name  = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
print("----------------")

#使用制表符或者换行符来添加空白
print("---------添加空白------------")
print("python")
print("\tpython")
print("Language:\nPython\nC\nJavaScript")
print("--------------------------")

#删除多余的空白
print("---------删除多余的空白---------")
message = " Python "
print(message)
print(message.rstrip())
print(message.lstrip())
print(message.strip())

