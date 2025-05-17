# print('丘吉尔说：“成功就是失败到失败，也依然不改热情！”')
#
# print("My favorite sports are as follows:\n\tfootball\n\trable tennis\n\tswimming\n running")
#
# print("my favorite sports are as follows:")
# print(str("\tfootball\n\t rable tennis\n\tswimmingn\n ").upper())
#
# a = 10
# b = 20
# c = 30
# sum = a + b + c
# print("sum=", sum)
# print("p=", sum / 3)
#
# print("%s\t%.1f\t%d\t%.2f" % ("dora", 899, 10, 899 / 10))
#
# # chickenrabbit.py
# iHeads = 35
# iFeet = 94
# a = iFeet - 2 * iHeads
# iRabbits = a / 2
# iChicken = iHeads - iRabbits
# print("Number of chicken=%d," % iChicken, "Numbre of rabbits=%d" % iRabbits)
# print(iFeet == iChicken * 2 + iRabbits * 4)
#
# # input.py
# a = int(input("how C it is:"))
# print("c=", 5 / 9 * (a - 32))
#
# b = int(input("num1:"))
# c = int(input("num2:"))
# print("num=", b + c)
# print("n=", (b + c) / 2)
#
# r = int(input("r="))
# print("C=", 3.14 * r * 2)
# print("S=", 3.14 * r * r)
#
# spam = ['aaa', 'sss', 'ddd', 'qqq', 'www', 'eee', 'fff', 'ggg']
# for i in range(len(spam)):
#     print('第' + str(i) + '个元素是：' + spam[i])
# print()
# print(spam.index('ddd'))
# print()
# for index, elem in enumerate(spam):
#     print('第' + str(index) + '个元素是' + elem)
# print()
# print(list(enumerate(spam)))
#
# lists = [1, 1, 2, 3, 4, 6, 9, 6, 2, 2]
# lists.sort()
# t = lists[-1]
#
# for i in range(len(lists) - 2, -1, -1):
#     if t == lists[i]:
#         lists.remove(lists[i])
#     else:
#         t = lists[i]
#         print(lists[i])
# import numpy as np
#
# lists = [1, 1, 2, 3, 4, 6, 9, 6, 2, 2]
# lists = np.unique(lists)
# print(list[i])
# from _ast import operator
#
# w = int(input("weight="))
# print("体重是:%d千克" % w)
# h = float(input("high="))
# print("身高是:%.2f米" % h)
# BMI = int(w / (h * h))
# print("BMI为", BMI)
# if BMI < 18:
#     print('超轻')
# if 18 <= BMI < 25:
#     print('标准')
# if 25 <= BMI < 27:
#     print('超重')
# if 27 <= BMI:
#     print("肥胖")
#
# from collections import Counter
#
#
# def count_each_char(str):
#     dict = {}
#     for i in str:
#         dict[i] = dict.get(i, 0) + 1
#     return dict
#
#
# if __name__ == "__main__":
#     res = count_each_char("python,computer,book,program")
#     print(res)

# phoneBook.py
phoneBook1 = {"name": "张三", "english": 80, "python": 90, "math": 100}
phoneBook2 = {"name": "李四", "english": 70, "python": 80, "math": 110}
phoneBook3 = {"name": "王五", "english": 60, "python": 70, "math": 120}
phoneBook4 = {"name": "武六", "english": 50, "python": 60, "math": 130}
phoneBook5 = {"name": "赵七", "english": 40, "python": 50, "math": 140}
scores = {phoneBook1, phoneBook2, phoneBook3, phoneBook4, phoneBook5}
print(scores)
# update.py
phoneBook6 = {"name": "张三", "english": 80, "python": 90, "math": 100, "avg": 90}
phoneBook1.update(phoneBook6)
phoneBook7 = {"name": "李四", "english": 70, "python": 80, "math": 110, "avg": 86}
phoneBook2.update(phoneBook7)
phoneBook8 = {"name": "王五", "english": 60, "python": 70, "math": 120, "avg": 83}
phoneBook3.update(phoneBook8)
phoneBook9 = {"name": "武六", "english": 50, "python": 60, "math": 130, "avg": 80}
phoneBook4.update(phoneBook9)
phoneBook10 = {"name": "赵七", "english": 40, "python": 50, "math": 140, "avg": 78}
phoneBook5.update(phoneBook10)
print(phoneBook1)
print(phoneBook2)
print(phoneBook3)
print(phoneBook4)
print(phoneBook5)
scores.sort(key="avg", reverse=True)
print(scores)
