#数字

#进行加减乘乘除、乘方运算
print(2+3)
print(2**3)

#支持运算次序
print(2 + 3 * (5 - 1))

#支持浮点数运算,但包含小数的位数不确定
print(0.1 + 0.01)

#使用str()避免类型错误，可以将数字23转换成字符串23
age = 23
#print("Happy " + age + "rd Birthday!")
print("Happy " + str(age) + "rd Birthday!")
