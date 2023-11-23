# money=99
# count=5
# person='李强'
# print(money)
# print(count)
# print(person)
# money=9.99
# print(money,type(money))
# money=9
# print(money,type(money))
# money='9.9$'
# print(money,type(money))
#
# name='小白'
# sex='man'
# age='sixteen'
# tn='191110119120'
# print(name,'今年',age,'性别',sex,'电话号码',tn)
#
# print('曾经有一份真挚的爱情摆在我面前，')
# print('我没有去珍惜,')
# print('直到失去了我才后悔莫及.')
# print('如果上天能给我一个再来一次的机会，')
# print('我希望能给那个女孩说我爱你。')
# print('如果要对这份爱加一个期限，')
# print('我希望是一万年。')
# print('')
# print(' ***** *****')
# print(' ******* *******')
# # print(' ******************')
# # print(' ****************')
# # print(' ************')
# # print(' ********')
# # print(' **')
# #
# # str='15615649156496'
# # print(str)
# # print(str[0:1])
# # print(str[2:8])
# # print(str[2:])
# # print(str[0:9:1])
# #
# # lst=[23,56,8,900,24]
# # lst.remove(8)
# # lst.append(30)
# # lst.insert(1,22)
# # lst.extend([66,90])
# # lst.pop(2)
# # lst.pop()
# # lst.sort()
# # lst.reverse()
# # print(lst)
# #
#
# import time
# curtime = time.time()
# totalSeconds = int(curtime)
# cursecond =totalSeconds % 60
# totalminutes = totalSeconds//60
# curminute=totalSeconds%60
# totalhours=totalminutes//60
# curhour =totalhours%24
# print("现在是北京时间",curhour,"时",curminute,"分", cursecond,"秒","1970年1月1日到现在经过了",totalSeconds,"秒")
#
# import datetime
# curdate=datetime.datetime.now()
# print(curdate.year,"-",curdate.month,"-",curdate.day,"\n",curdate.hour,":",curdate.minute,":",curdate.second)
# print(type(curdate))
#
# n1=pow(2,8)
# n2=abs(-22)
# n3=round(7/2)
# print("2^8=",n1)
# print("absolute value of -10=",n2)
# print("7/2~~",n3)
#
# def costcompute(istart,iend):
#     iconsume =iend-istart
#     return iconsume*0.85
# felecfeel1=costcompute(1201,1786)
# felecfeel2=costcompute(1322,1423)
# print("electronic power cost of mrzhaang:",felecfeel1)
# print("electronic power cost of mr lee:",felecfeel2)
#
# import math
# from math import sqrt
# print(math.floor(67.8))
# print(math.ceil(78.4))
# print(math.sqrt(10))
# print(sqrt(20))
#
# sname =input("what's your name:")
# iage=input("how old are you?")
# iage=int(iage)
# print("hi,",sname,",","you are",iage,"years old")
#
# sname="mary"
# fprice=125.75
# n=5
#
# a=0xff
# b=0b0111
# print("oxff=",a,",","0b0111=",b)
# print(a,"=",hex(a),",",b,"=",bin(b))
# print("%x"%(255))
#
# months =['january','february','march','april','may','june','july','august','september','october','november','december']
# print(type(months))
# print(len(months))
# print(months[0],months[3])


# variable.py
# n=5
# fprice=4.8
# fAmount=n*fprice
# fMoney=30
# fMoney=fMoney-fAmount
# sText="我已经买了"
# print(sText,n,"斤苹果，每斤4.8元，一共花了",fAmount,"元。","给了我30元，还剩下",fMoney,"元")
age = int(input("请输入你的年龄:"))
if 0 < age <= 2:
    print("婴儿")
elif 2 < age <= 6:
        print("幼儿")
elif 6 < age <= 11:
         print("少儿") 
elif 11 < age <= 15:
    print("少年")
elif 15 < age <= 18:
    print("青年")
elif 18 < age <= 30:
    print("成年")
elif 30 < age <= 50:
    print("中年")
elif 50 < age <= 100:
    print("老年")
else:
    print("老不死")
