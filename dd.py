# # money=99
# # count=5
# # person='李强'
# # print(money)
# # print(count)
# # print(person)
# # money=9.99
# # print(money,type(money))
# # money=9
# # print(money,type(money))
# # money='9.9$'
# # print(money,type(money))
# #
# # name='小白'
# # sex='man'
# # age='sixteen'
# # tn='191110119120'
# # print(name,'今年',age,'性别',sex,'电话号码',tn)

# # # str='15615649156496'
# # # print(str)
# # # print(str[0:1])
# # # print(str[2:8])
# # # print(str[2:])
# # # print(str[0:9:1])
# # #
# # # lst=[23,56,8,900,24]
# # # lst.remove(8)
# # # lst.append(30)
# # # lst.insert(1,22)
# # # lst.extend([66,90])
# # # lst.pop(2)
# # # lst.pop()
# # # lst.sort()
# # # lst.reverse()
# # # print(lst)
# # #
# #
# # import time
# # curtime = time.time()
# # totalSeconds = int(curtime)
# # cursecond =totalSeconds % 60
# # totalminutes = totalSeconds//60
# # curminute=totalSeconds%60
# # totalhours=totalminutes//60
# # curhour =totalhours%24
# # print("现在是北京时间",curhour,"时",curminute,"分", cursecond,"秒","1970年1月1日到现在经过了",totalSeconds,"秒")
# #
# # import datetime
# # curdate=datetime.datetime.now()
# # print(curdate.year,"-",curdate.month,"-",curdate.day,"\n",curdate.hour,":",curdate.minute,":",curdate.second)
# # print(type(curdate))
# #
# # n1=pow(2,8)
# # n2=abs(-22)
# # n3=round(7/2)
# # print("2^8=",n1)
# # print("absolute value of -10=",n2)
# # print("7/2~~",n3)
# #
# # def costcompute(istart,iend):
# #     iconsume =iend-istart
# #     return iconsume*0.85
# # felecfeel1=costcompute(1201,1786)
# # felecfeel2=costcompute(1322,1423)
# # print("electronic power cost of mrzhaang:",felecfeel1)
# # print("electronic power cost of mr lee:",felecfeel2)
# #
# # import math
# # from math import sqrt
# # print(math.floor(67.8))
# # print(math.ceil(78.4))
# # print(math.sqrt(10))
# # print(sqrt(20))
# #
# # sname =input("what's your name:")
# # iage=input("how old are you?")
# # iage=int(iage)
# # print("hi,",sname,",","you are",iage,"years old")
# #
# # sname="mary"
# # fprice=125.75
# # n=5
# #
# # a=0xff
# # b=0b0111
# # print("oxff=",a,",","0b0111=",b)
# # print(a,"=",hex(a),",",b,"=",bin(b))
# # print("%x"%(255))
# #
# # months =['january','february','march','april','may','june','july','august','september','october','november','december']
# # print(type(months))
# # print(len(months))
# # print(months[0],months[3])
# #
# # #variable.py
# # n=5
# # fprice=4.8
# # fAmount=n*fprice
# # fMoney=30
# # fMoney=fMoney-fAmount
# # sText="我已经买了"
# # print(sText,n,"斤苹果，每斤4.8元，一共花了",fAmount,"元。","给了我30元，还剩下",fMoney,"元")

#切片(取左不取右)
name="愿神龙指引我的箭"
print(name[0:3])
print(name[-3:-1])
#切片步长
print(name[0::3])

name1="尝尝神龙之剑"
name2="天降正义"
name3="天行健"
name4="君子以自强不息"
name5="地承坤"
name6="君子以德载物"
print(name1[2:6])
print(name,name1,name2,name3,name4,name5,name6,sep=',')
print(name,name1,name2,name3,name4,sep=',',end='。')
print(name5,name6)

#双引号的打印
name7= '半藏:"龙啊！请吞噬我的敌人吧~"'
print(name7)

# import turtle
# def flyTo(x, y):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#
#
# def drawEye():
#     turtle.tracer(False)
#     a = 2.5
#     for i in range(120):
#         if 0 <= i < 30 or 60 <= i < 90:
#             a -= 0.05
#         else:
#             a += 0.05
#         turtle.left(3)
#         turtle.fd(a)
#     turtle.tracer(True)
#
#
# def beard():
#     """ 画胡子， 一共六根
#     """
#     # 左边第一根胡子
#     flyTo(-37, 135)
#     turtle.seth(165)
#     turtle.fd(60)
#
#     # 左边第二根胡子
#     flyTo(-37, 125)
#     turtle.seth(180)
#     turtle.fd(60)
#
#     # 左边第三根胡子
#     flyTo(-37, 115)
#     turtle.seth(193)
#     turtle.fd(60)
#
#     # 右边第一根胡子
#     flyTo(37, 135)
#     turtle.seth(15)
#     turtle.fd(60)
#
#     # 右边第二根胡子
#     flyTo(37, 125)
#     turtle.seth(0)
#     turtle.fd(60)
#
#     # 右边第三根胡子
#     flyTo(37, 115)
#     turtle.seth(-13)
#     turtle.fd(60)
#
#
# def drawRedScarf():
#     """ 画围巾
#     """
#     turtle.fillcolor("red")  # 填充颜色
#     turtle.begin_fill()
#     turtle.seth(0)  # 朝向右
#
#     turtle.fd(200)  # 前进10个单位
#     turtle.circle(-5, 90)
#
#     turtle.fd(10)
#     turtle.circle(-5, 90)
#
#     turtle.fd(207)
#     turtle.circle(-5, 90)
#
#     turtle.fd(10)
#     turtle.circle(-5, 90)
#
#     turtle.end_fill()
#
#
# def drawMouse():
#     flyTo(5, 148)
#     turtle.seth(270)
#     turtle.fd(100)
#     turtle.seth(0)
#     turtle.circle(120, 50)
#     turtle.seth(230)
#     turtle.circle(-120, 100)
#
#
# def drawRedNose():
#     flyTo(-10, 158)
#     turtle.fillcolor("red")  # 填充颜色
#     turtle.begin_fill()
#     turtle.circle(20)
#     turtle.end_fill()
#
#
# def drawBlackdrawEye():
#     turtle.seth(0)
#     flyTo(-20, 195)
#     turtle.fillcolor("#000000")  # 填充颜色
#     turtle.begin_fill()
#     turtle.circle(13)
#     turtle.end_fill()
#     turtle.pensize(6)
#     flyTo(20, 205)
#     turtle.seth(75)
#     turtle.circle(-10, 150)
#     turtle.pensize(3)
#     flyTo(-17, 200)
#     turtle.seth(0)
#     turtle.fillcolor("#ffffff")
#     turtle.begin_fill()
#     turtle.circle(5)
#     turtle.end_fill()
#     flyTo(0, 0)
#
#
# def drawFace():
#     """
#     """
#     turtle.forward(183)  # 前行183个单位
#     turtle.fillcolor("white")  # 填充颜色为白色
#     turtle.begin_fill()  # 开始填充
#     turtle.left(45)  # 左转45度
#     turtle.circle(120, 100)  # 右边那半边脸
#     turtle.seth(90)  # 朝向向上
#     drawEye()  # 画右眼睛
#     turtle.seth(180)  # 朝向左
#     turtle.penup()  # 抬笔
#     turtle.fd(60)  # 前行60
#     turtle.pendown()  # 落笔
#     turtle.seth(90)  # 朝向上
#     drawEye()  # 画左眼睛
#     turtle.penup()  # 抬笔
#     turtle.seth(180)  # 朝向左
#     turtle.fd(64)  # 前进64
#     turtle.pendown()  # 落笔
#     turtle.seth(215)  # 修改朝向
#     turtle.circle(120, 100)  # 左边那半边脸
#     turtle.end_fill()  #
#
#
# def drawHead():
#     """ 画了一个被切掉下半部分的圆
#     """
#     turtle.penup()  # 抬笔
#     turtle.circle(150, 40)  # 画圆, 半径150，圆周角40
#     turtle.pendown()  # 落笔
#     turtle.fillcolor("#00a0de")  # 填充色
#     turtle.begin_fill()  # 开始填充
#     turtle.circle(150, 280)  # 画圆，半径150, 圆周角280
#     turtle.end_fill()
#
#
# def drawAll():
#     drawHead()
#     drawRedScarf()
#     drawFace()
#     drawRedNose()
#     drawMouse()
#     beard()
#     flyTo(0, 0)
#     turtle.seth(0)
#     turtle.penup()
#     turtle.circle(150, 50)
#     turtle.pendown()
#     turtle.seth(30)
#     turtle.fd(40)
#     turtle.seth(70)
#     turtle.circle(-30, 270)
#     turtle.fillcolor("#00a0de")
#     turtle.begin_fill()
#     turtle.seth(230)
#     turtle.fd(80)
#     turtle.seth(90)
#     turtle.circle(1000, 1)
#     turtle.seth(-89)
#     turtle.circle(-1000, 10)
#     turtle.seth(180)
#     turtle.fd(70)
#     turtle.seth(90)
#     turtle.circle(30, 180)
#     turtle.seth(180)
#     turtle.fd(70)
#     turtle.seth(100)
#     turtle.circle(-1000, 9)
#     turtle.seth(-86)
#     turtle.circle(1000, 2)
#     turtle.seth(230)
#     turtle.fd(40)
#     turtle.circle(-30, 230)
#     turtle.seth(45)
#     turtle.fd(81)
#     turtle.seth(0)
#     turtle.fd(203)
#     turtle.circle(5, 90)
#     turtle.fd(10)
#     turtle.circle(5, 90)
#     turtle.fd(7)
#     turtle.seth(40)
#     turtle.circle(150, 10)
#     turtle.seth(30)
#     turtle.fd(40)
#     turtle.end_fill()
#
#     # 左手
#     turtle.seth(70)
#     turtle.fillcolor("#FFFFFF")
#     turtle.begin_fill()
#     turtle.circle(-30)
#     turtle.end_fill()
#
#     # 脚
#     flyTo(103.74, -182.59)
#     turtle.seth(0)
#     turtle.fillcolor("#FFFFFF")
#     turtle.begin_fill()
#     turtle.fd(15)
#     turtle.circle(-15, 180)
#     turtle.fd(90)
#     turtle.circle(-15, 180)
#     turtle.fd(10)
#     turtle.end_fill()
#     flyTo(-96.26, -182.59)
#     turtle.seth(180)
#     turtle.fillcolor("#FFFFFF")
#     turtle.begin_fill()
#     turtle.fd(15)
#     turtle.circle(15, 180)
#     turtle.fd(90)
#     turtle.circle(15, 180)
#     turtle.fd(10)
#     turtle.end_fill()
#
#     # 右手
#     flyTo(-133.97, -91.81)
#     turtle.seth(50)
#     turtle.fillcolor("#FFFFFF")
#     turtle.begin_fill()
#     turtle.circle(30)
#     turtle.end_fill()
#
#     # 口袋
#     flyTo(-103.42, 15.09)
#     turtle.seth(0)
#     turtle.fd(38)
#     turtle.seth(230)
#     turtle.begin_fill()
#     turtle.circle(90, 260)
#     turtle.end_fill()
#     flyTo(5, -40)
#     turtle.seth(0)
#     turtle.fd(70)
#     turtle.seth(-90)
#     turtle.circle(-70, 180)
#     turtle.seth(0)
#     turtle.fd(70)
#
#     # 铃铛
#     flyTo(-103.42, 15.09)
#     turtle.fd(90)
#     turtle.seth(70)
#     turtle.fillcolor("#ffd200")
#     turtle.begin_fill()
#     turtle.circle(-20)
#     turtle.end_fill()
#     turtle.seth(170)
#     turtle.fillcolor("#ffd200")
#     turtle.begin_fill()
#     turtle.circle(-2, 180)
#     turtle.seth(10)
#     turtle.circle(-100, 22)
#     turtle.circle(-2, 180)
#     turtle.seth(180 - 10)
#     turtle.circle(100, 22)
#     turtle.end_fill()
#     flyTo(-13.42, 15.09)
#     turtle.seth(250)
#     turtle.circle(20, 110)
#     turtle.seth(90)
#     turtle.fd(15)
#     turtle.dot(10)
#     flyTo(0, -150)
#     drawBlackdrawEye()
#
#
# def main():
#     turtle.screensize(800, 6000, "#F0F0F0")
#     turtle.pensize(3)
#     turtle.speed(9)
#     drawAll()
#
#
# if __name__ == "__main__":
#     main()
#     turtle.mainloop()
