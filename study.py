# #sep与end的作用
name1 = '源氏说:"尝尝神龙之剑"'
name2 = '半藏说："愿神龙指引我的箭'
print(name2[0::1])
# name3="命运的齿轮在转动"
# name4='龙啊~请吞噬我的敌人"'
# name5="天行健"
# name6="君子以自强不息"
# name7="地承坤"
# name8="君子以德载物"
# print(name1,)
# print(name2,name4,sep=",")
# print(name5,name6,name7,name8,sep=",",end="。"'\n')

# 格式化输出
# name='A'
# age=18
# pho=132943245
# ten='星球'
# print('你是:%s,年龄:%d,电话号码:%d,来自于:%s' %(name,age,pho,ten),end='\n')
# print('先知曾经说过:{}，半藏曾经说过:{}，还有一个人{}'.format(name3,name4,name1))

# input输入
# role=input("请输入的你的名字:")
# age=input("请输入你的年龄:")
# high=input("请输入你的身高:")
# weight=input("请输入你的体重:")
# shop=input("请输入你想购买的商品:")
# print("你的名字:",role,"你的年龄:",age,"你的身高:",high,"你的体重:",weight)

# name='abc'
# name1=name
# name2=name1
# name3=name2
# print("name3=",name)

# a=10
# b=10
# print(a==b)
# c=20
# print(a+b==c)

# # 十进制转二进制
# a = 10
# print(bin(a))
# # 二进制转十进制
# a = 0b11011
# print(int(a))

# a = 3
# b = 4
# c = 5
# d = 6
# print(a & b)  # 与（见零为零 全一为一）
# #  00000011
# #  00000100
# # =00000000
# print(b | c)  # 或（见一为一 全零为零）
# #  00000100
# #  00000101
# # =00000101
# print(~c)  # 非（取反）
# # 00000101
# # =
# print(c ^ d)  # 异或（相同为零 不同为一）
# # 00000101
# # 00000110
# #=00000011
# # print(a>>1)#二进制右移一位 设x左/右移n位，则结果为x乘/除以2的n次方
# # 00000011
# #=00000001
# print(b<<1)#二进制左移一位
# # 00000100
# #=00001000
#
# #三目运算符
# result=(a*b)if(a>b)else(a/b)
# print(result)

# 字符串拼接
a = "qwertyuiop"
b = "asdfghjkl"
c = "zxcvbnm"
d=','.join((a,b,c))
print(a+b+c)
print(d)