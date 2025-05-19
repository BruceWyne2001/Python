# #sep与end的作用
# name1 = '源氏说:"尝尝神龙之剑"'
# name2 = '半藏说："愿神龙指引我的箭'
# print(name2[0::1])
# name3="命运的齿轮在转动"
# name4='龙啊~请吞噬我的敌人"'
# name5="天行健"
# name6="君子以自强不息"
# name7="地承坤"
# name8="君子以德载物"
# print(name1,)
# print(name2,name4,sep=",")
# print(name5,name6,name7,name8,sep=",",end="。"'\n')
#
#from audioop import lin2lin
#from random import random
#import  random
#格式化输出——电影票案例
# name='蝙蝠侠'
# ticket=9.5
# num=40
# total=ticket*num
# print('电影的名字叫{}，单价为{}，人数为{}，总价为{}'.format(name,ticket,num,total))
import random
from os import lseek

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
#负数换算
# b=-2
# print(bin(b))
# b=-0b100111
# print(int(b))

#八进制转十进制
# d=0o6630
# print(int(d))
#十进制转八进制
# d=100
# print(oct(d))

#十六进制转十进制
# d=0xcccd
# print(int(d))
#十进制转十六进制
# d=100
# print(hex(d))

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
# # 00000110
# print(c ^ d)  # 异或（相同为零 不同为一）
# # 00000101
# # 00000110
# #=00000011
# # print(a>>1)#二进制右移一位 设x左/右移n位，则结果为x乘/除以2的n次方
# # 00000011
# #=00000001
# print(b<<1)#二进制左移一位
# # 00000100
# #00001000

# #三目运算符
# result=(a*b)if(a>b)else(a/b)#if语句若为真（true），则打印前者，反之打印后者
# print(result)

# 字符串拼接
# a = "qwertyuiop"
# b = "asdfghjkl"
# c = "zxcvbnm"
# d=','.join((a,b,c))
# print(a+b+c)
# print(d)

#**普通数值打印:**
# s1=98.5013444
# print("我考了{:.1f}".format(s1))

#**百分比数值打印:**
# s1=0.2345567
# print('{:.1%}'.format(s1))
#
#**F表达式:**
# name = 'a'
# age = 0
# s1 = f'我的名字叫{name}，年龄为{age}'
# print(s1)

#列表的一般形式
# list1 = [1, 2, 34, 5, 6, 7, 8, 9, 0, 'ggb', [1, 2, 3, 4, 5, 6]]
# print(list1[1])
# print(list1[10][2])

#列表的更新
# list1=[1,2,34,5,6,7,8,9,0,'ggb',[1,2,3,4,5,6]]
# list1[3]=44
# print(list1)

#三国杀(蒸蒸日上)
# print('*'*20)
# print('欢迎来到三国杀,\n''你当前的级别为一，可免费游玩.......')
# print('*'*20)
# print('\n')
# print('现在你的等级为2，请充值30元继续游玩')
# money=int(input('充值金额：'))
#
# if money>=30:
#     print('充值成功，请继续游玩')
# elif 0<money<=30:
#     money1=30-money
#     print('请继续充值{}元,才可继续游玩'.format(money1))
# else:
#     print('请重试')

#range常规应用
# for i in range(4):
#     print(i)

#寻找1~100的8的倍数
# s = [x for x in range(1, 101) if x % 8 == 0 ]
# print(s)

#猜数字
# a=random.randint(1,10)
# for i in range(10):
#     num=int(input("请输入一个数字1~10:"))
#     if num== a:
#         print("恭喜你，猜对了！！！")
#         break
#     else:
#         print(("再来一次"))

#跳过毒馒头
# for i in range(1,11):
#     if i == 3:
#       continue
#     else:
#         print("我正在吃{}个馒头".format(i))

#for循环模拟登录
# nun="1520182685"
# num="jjj2001617"
# eve = input("请输入账号:")
# sve = input("请输入密码:")
# for i in range(10):
#   if eve!=nun:
#       eve=input("请重新输入账号:")
#   elif eve==nun and sve!=num:
#       sve=input("请重新输入密码:")
#   else:
#       print("登录成功！！！")
#       break

#简单while求和应用
# i=0
# tot=0
# while i<=100:
#   tot=tot+i
#   i+=2
# print(tot)

#while求数
# num=0
# while num<=100:
#     if num%6==0 and num!=0:
#         print(num)
#         num+=1
#     else:
#         num+=1

#while画等边三角形
# a=int(input("请输入数值"))
# num=1
# print(' '*a,'*'*num,' '*a)
# b=1
# a=a-2
# while b<a:
#     print(' '*a,'*',' '*b,'*')
#     a=a-1
#     b=b+2
# print(' '*a,"*"*(b+4))

# 模拟赌场
# money=12
# a=input("是否进入游戏:(是/否)")
# if a=='是':
#     print("现在开始游戏，您目前有{}个金币,每次游戏会自动支付2个金币".format(money))
#     again = '是'
#     while again == '是'and money>0:
#         money-=2
#         a1 = random.randint(1, 6)
#         a2 = random.randint(1, 6)
#         guess = input("请猜大小:(大/小)")
#         if (a1 + a2 > 6 and guess == '大') or (a1 + a2 <= 6 and guess == '小'):
#             print("你猜对了！！！！，获得3个金币")
#             money=money+3
#             again = input("是否继续游玩(是/否)，你目前的金币数量为{}:".format(money))
#         elif money==0:
#             money1=int(input("金币不足，请充值:(0默认为不充值)"))
#             money==money1+money
#             if money==0:
#                 break
#             else:
#                 pass
#         else:
#             print("可惜，你猜错了...你目前的金币数量为{}:".format(money))
#             again = input("是否继续游玩:")
# else:
#    pass

#输出0-100中偶数的和
# a=0
# total=0
# while a<100:
#     a+=2
#     total=a+total
# print("偶数的总和为:{}".format(total))

#字符串的拼接
# s1='hello'
# s2='world'
# s3=s1+s2
# print(s3)

#字符串的倍数
# s1='hello '
# s2=s1*5
# print(s2)

#字符串位置判断
# s1 = 'hello,world'
# result1 = 'he' in s1
# result2 = 'wr' in s1
# print(result1)
# print(result1)

#字符串格式化打印
#%
# name1 = 'bruce'
# name2 = 'bary'
# sp = 'i m rich'
# print('%s对%s 说：我的超能力是%s' %(name1,name2,sp))

#指定获取字符串
# a = 'hello,wor6ld，goodmorning'
# print(a[0:15])
# print(a[0:15:3])
# print(a[-1:11:-1])
# print(a[::-1])
# print(a[11:-1])
# print(a[-1:-8:-2])

#字符串内嵌函数
# message = 'my name is kk and come form china'
# messg = message.capitalize( )
# messg1=message.title()
# messg2=message.istitle()
# messg3=message.upper()
# messg4=message.isupper()
# messg5=message.lower()
# messg6=message.islower()
# messg7=len(message)
# print(messg)
# print(messg1)
# print(messg2)
# print(messg3)
# print(messg4)
# print(messg5)
# print(messg6)
# print(messg7)

#模拟验证码
# code=''
# times = 1
# a='ZXCVBNMASDFGHJKLQWERTYUIOPqwertyuiopasdfghjklzxcvbnm0123456789'
# while times<5:
#     ran=random.randint(0,len(a)-1)
#     code+=a[ran]
#     times+=1
# print('验证码为：{}'.format(code))
# ves=1
# while ves ==1:
#     incode = input("请输入你的验证码:")
#     if code==incode:
#         print("登录成功")
#         break
#     else:
#         print("验证码输入错误")
#         ves==1

#字符串查找函数
# s1='sdadgsdgrwfewqrewywoithgdksjvnbch'
# a=input("请输入需要查找的字符:")
# length=(len(s1))
# print(length)
# position=s1.find(a)#find函数
# print("找到了，在第{}个下标！".format(position))
# b=position
# while b<length:
#     position=s1.find(a,b)
#     if position>0:
#         print("找到了，在第{}个下标！".format(position))
#         b = position
#         b+=1
#     else:
#         pass
# else:
#     pass

#"输入两个字符串，从第一个字符中删除第二个字符串中所有的字符"
#"例如 输入“qweasdzxc”和“qwertyuiop”，则输出的字符串就是“rtyuiop”"
# s1=input("请输入第一字符串：")
# s2=input("请输入第二字符串：")
# a1=''
# for i in s1:
#       if i in s2:
#         pass
#       else:
#            a1+=i
# print(a1)

#"输入两个字符串，从长字符串中删除短字符串中所有的字符"
# s1=input("请输入第一字符串：")
# s2=input("请输入第二字符串：")
# l1=len(s1)
# l2=len(s2)
# a1=''
# if l2>l1:
#         s1,s2=s2,s1
# for i in s1:
#       if i in s2:
#         pass
#       else:
#            a1+=i
# print(a1)

# a1=0
# a2=0
# for i in s1:
#         a1+=1
# for i in s2:
#         a2+=1

# s1=input("请输入字符串:")
# for i in range (len(s1)):
#   if s1[i]<'A' or s1[i]>'Z':
#       print("不喜欢")
#       break
# else:
#     if s1[i-1]==s1[i]:
#         print("不喜欢")
#
#     else:
#         print("喜欢")

# s2='dfghjkl;dasdweqwr'
# b=s2.rfind('d')#rfind函数
# print(b)
# c=s2[b::]#查找当前字符后面的字符
# print(c)
# b1=s2.replace('d','D',)#replace函数
# print(b1)

# s3='奈克瑟斯奥特曼,诺亚奥特曼,奈欧斯奥特曼，欧布奥特曼，乔尼亚斯奥特曼，阿斯特拉奥特曼'
# b2=s3.encode()#encode函数
# print(b2)
# c2=b2.decode()#decode
# print(c2)

#starswith函数与endswith函数
# s1='bijiben200000000000.ini'
# d1=s1.startswith('biji')
# d2=s1.startswith('bj')
# d3=s1.endswith('ini')
# d4=s1.endswith('doc')
# print(d1,d2,d3,d4)

# s2=input("请输入你想要输入的字符:")
# s3=input("请输入你想要输入的字符:")
# s4=input("请输入你想要输入的字符:")
# d1=s2.isalnum()
# d2=s3.isalnum()
# d3=s4.isalnum()
# d4=s2.isalpha()
# d5=s3.isalpha()
# d6=s4.isalpha()
# d7=s2.isdigit()
# d8=s3.isdigit()
# d9=s4.isdigit()
# print(d1,d2,d3,d4,d5,d6,d7)

# s1='——'.join('奥特曼')
# print(s1)

# s1='sdas     dqweasdqwes'
# d1=s1.lstrip('s')
# d2=s1.rstrip('s')
# d3=s1.strip('s')
# # print(d1)
# print(d2)
# print(d3)

# s1='helloworld,hellosky,helloriver'
# d1=s1.split(',',3)
# print(d1)
#
# 列表的简单应用
# names = ['ultraman','batman','optimus prime','gumdan','master chief']
# list=['ultraman','batman','奈克瑟斯','optimus prime','奈克瑟斯','gumdan','master chief','奈克瑟斯']
# for name in names:
#     print(name,sep='',end=',')
# print(end='\n')

# #列表元素的替换
# for name in list:
#     print(name,sep='',end=',')
# print(end='\n')
#
# for i in (len(list)):
#     print(i,sep='',end=',')
#     if '奈克瑟斯'in list[i]:
#         list[i] = 'nexus'
# print(end='\n')

# # #简单删除操作
# del list[2]
# print(list)
# print(end='\n')
# l=len(list)
# i=0
# # #循环与删除列表
# while i<l:
#     if 'batman'in list[i] or 'superman' in list[i]:
#         del list[i]
#         l-=1
#     i+=1
# print(list)

#自定义删除
# word=['app','abb','add','edd','epp','bbs','gdd','err','tyuu']
# lei=input("请输入设定的字符:")
# i=0
# l=len(word)
# while i<l:
#     if lei in word[i]:
#         del word[i]
#         l-=1
#         continue
#     i+=1
# print(word)

#列表的拆分
# list1=['杰克','初代','佐菲','赛文','艾斯','泰罗','梦比优斯','雷欧','爱迪','乔尼亚斯',99.8,1000000,'qweasdzxc']
# l1=list1[0:10]
# print(l1)
# list2=['杰克','初代','佐菲','赛文','艾斯','泰罗','梦比优斯','雷欧','爱迪','乔尼亚斯','赛文X','赛文21','利奥','帕瓦特',99.8,1000000,'qweasdzxc']
# l2=list2[::2]
# print(l2)
# l3=list2[-1:-10:-2]
# print(l3)

# 列表的追加
# list1= ['杰克', '初代', '佐菲', '赛文', '艾斯', '泰罗', '梦比优斯', '雷欧', '爱迪', '乔尼亚斯', 99.8, 1000000,
#         'qweasdzxc', '赛文X', '赛文21', '利奥', '帕瓦特']
# add=['赛文X','赛文21','利奥','帕瓦特']
# list1.append(add)#append
# print('list1=',list1)
# list1.extend(add)#extend
# print('list1=',list1)
# list1=list1+add
# print('list1=',list1)
# list1.insert(2,'奥特曼')#insert
# print('list1=',list1)

# #生成随机数，并判断随即数是否在固定数列表中
# list2=[10,20,30,40,50,60,70,15,26,33,47,57]
# for i in range(50):
#         ran=random.randint(1,100)
#         if ran!=list2:
#                 print("打印随机数:",ran)
#         else:
#                 break


# random_list=[]
# i=0
# #while i<20:
# for i in range(20):
#     ran = random.randint(1,100)
#     random_list.append(ran)
#     i+=1
#     print(random_list)
    #升/降序排列
# up_list=sorted( random_list)
# down_list=sorted(random_list,reverse=True)
# print('升序是：',up_list)
# print('降序是：',down_list)
#取最大/最小值
# mxvale=random_list[0]
# # mvale=random_list[0]
# for vale in random_list:
#
#     if vale > mxvale:
#         mxvale=vale
#         print("最终最大值为:",mxvale)
#     if vale > mvale:
#         vale = mvale
# print("最终最小值为:",mvale)
#等同于下面代码
# random_end=max(random_list)
# print(random_end)
#random_end=min(random_list)
# print(random_end)

#列表简单运用
# l1=[1,2,3]
# l2=[4,5,6]
# l3=l1+l2
# l4=[1,2,3,'a','b',[1],[2,3],'奥特曼']
# a1=l1*4
# print(l3)
# print(a1)
# b1=4 in l1
# print(b1)
# c1=[1] in l4
# print(c1)

#已知字符串A=“asmr3sdaFDSG456GSsdaF1S”,要求将A中字符串中大写转小写，小写转大写：
# A='asmr3sdaFDSG456GSsdaF1S'
# S=''
# for i in A:
#     if i.isupper():
#         S+=i.lower()
#     elif i.islower():
#         S+=i.upper()
#     else: S+=i
# print(A)
# print(S)
# W=S.lower()
# print(W)

# X='ABC'
# Y='CDE'
# Z=['F','G','H']
# A=X.join(Y)
# print(A)
# B=Y.join(Z)
# print(B)



