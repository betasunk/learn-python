# 数据类型
    # 字符串
    # 数字类型

# 判断数据类型的语句 type()

# mystr="黑马"
# print(type(mystr))

# 数据类型的转换
n=123
f=12.2222
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
x=b'ABC'.decode('ascii')
print(x)

y=b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(y)