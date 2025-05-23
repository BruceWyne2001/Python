# Python笔记
Python是**面向对象**的**解释型/弱类型**的程序。<br>
# 面向对象:
每一个变量都是一个类，有其自己的属性（attribute）与方法（method）。<br>
# 语法块：
用缩进（四个空格）而不是分号、花括号等符号来标记。因此，行首的空格不能随意书写。<br>
# 注释：
行内用“#”号，行间注释写在两组连续三单引号之间：’’’,<br>
# 续行： 
行尾输入一个反斜杠加一个空格（’\ ‘），再换行。如果行尾语法明显未完成（比如以逗号结尾），可以直接续行。<br>
# 打印与输入： 
函数 print() 与 input()，注意 print() 的 sep 与 end 参数。<br>

# 变量命名规则：
1 变量**只能是字母数字和下划线的任意组合**；<br>
2 变量名**第一个字符不能是数字**；<br>
3 变量名**区分大小写**，大小写字母背认为是两个不同的字符；<br>
4 **特殊关键字不能当变量名**（查看关键字：import keyword print（keyword.kwilist））；<br>
5 注意要写标识符（**见词知意**）；<br>

Sep=‘’为辨识分隔符（默认为空格）。<br>
End=‘’为辨识结束符（默认换行）。<br>
id：可查看当前变量在内存中的地址<br>

# 转义字符：
**\n**(全称为newline，开个新行) **\t**(制表符，等同于tab) **\r**(全称为carriage return，打印头回到行首。)如果没有\n直接\r，那么这行就直接被覆盖打印了。<br>   
Python数据类型：python具有六种数据类型： 不可变数据—— number（数字） string（字符串）tuple（元组）<br> 
可变数据——list（列表） sets（集合） dictionary（字典）。<br>
**\n:** 换行;  **\t:** 制表符（四个空格的位置）;  **\r:** 覆盖（后者覆盖前者） **\b:** 删除（一个b等于一个BakeSpace); 
两个‘\\’可以在输出中出现一个‘\’; <br>   原字符：在字符串的前面加上**r（R）** 就会使转义字符失去作用。**“‘’”（三引号）:** 自定义格式输出。
**Type（变量名）**——测试变量是什么类型。<br>
**id:** 查看变量所处内存地址<br>

**切片:**

    name2='半藏说："愿神龙指引我的箭'
    print(name2[x:y:z])
在此代码[x:y:z]中，x指的是开始字符下标(若没有则从头开始取)，
y为结束字符下标(若没有则为最后一个字符下标)，z为顺序(默认为1，若为2则间接1个字符下标取值)

字符类型：%d为整型，%s字符串类型，%f为浮点数类型。
**格式化输出:**
Format是一个字符串的函数，适用于字符串的格式化， ‘’.format中的‘.’表示调用。<br>
默认调用的顺序是0,1,2<br>

**普通数值打印:**

    s1=98.5013444
    print("我考了{:.1f}".format(s1))
其中 **':.1f'** 表示纯浮点数的字符串保留1位小数。

**百分比数值打印:**

    s1=0.2345567
    print('{:.1%}'.format(s1))
其中 **':.1%'** 表示保留一位小数的百分比打印。

    s1='a %s b'%('x')  
    s2='a %d b%(100)'
    s3='a %f b%(1.1)
%s可以为所有的字符类型占位，%d为数值类型占位，%f为浮点数类型占位。

 **F表达式:**
     
    name='a'
    age=0
    s1=f'我的名字叫{name}，年龄为{age}'
Input默认的输出类型是***str***(input为阻塞式)

'&'为与运算（***见零为零 全一为一***），'|'为或运算（***见一为一 全零为零***），
'~'为非运算（***取反***） '^'为异或运算（***相同为零 不同为一***）<br>    
**区分**:=与==  前者为赋值，后者为相比<br>
**字符串操作:** 1、字符串的拼接:用'+'号将两个字符串连接在一起

    s1='xxxx'
    s2='tttttt'
    s3=s1+s2
    print(s3)

   2、字符串的倍数：用'*'号增加字符串出现的次数

    s1='xxxx'
    s2=s1*5
    print(s2)

   3、字符串位置判断：用'in'函数判断某个字符是否在字符串中

    s1='hello,world'
    result1='he' in s1
    result2='wr' in s1
    print(result1)
    print(result1)

   4、字符串格式化打印:使用%s、%d、%f等占位符对字符串进行指定打印
     
    name1 = 'xxx'
    name2 = 'ccc'
    sp = 'i m rich'
    print('%s对%s 说：我的超能力是%s' %(name1,name2,sp))

   5、指定获取字符:通过'[a:b]''[x:y:2]''[::2]'来获取字符串中指定的字符(方向要一致)
 
    a='abcdefg,hijklmn'
    print(0:8:2)

# 字符串内建函数: 声明一个字符串，默认可以调用内建函数，即系统已经备好的函数。
**capitalize函数:** 将字符串的第一个字母转为大写

    messg=message.capitalize()

**title函数:** 将字符串中的每个字符的首字母大写

    messg=message.title()

**istitle函数:** 判断字符串中的每个字符的首字母是否大写

    messg=message.istitle()

**upper函数:`** 将字符串中的字符全部转大写

    messg=message.upper()

**isupper函数:** 判断字符串中的字符是否全部转大写

    messg=message.isupper()

**lower函数:** 将字符串中的字符全部转小写

    messg=message.lower()

**islower函数:** 判断字符串中的字符是否全部转小写

    messg=message.islower()

**三目运算符:**
如果if成立，则运行if前面的，如果不成立，则运行else后面的。        

    result=(a*b)if(a>b)else(a/b)

**if语句:**
单分支————

    if 条件语句:(如果条件为真则打印结果)
        print(结果)
 如果被判断的语句为空，则默认为零（即假）
 如果，被判断的语句不为空，但条件语句为空，则默认为1（即真）

多分支————

    if 条件语句:(如果条件为真则打印结果)
        print(结果)
    elif 条件语句:(上述不成功，此条件成立，则打印此句结果)
        print(结果)
    .............................................  
    else 
       print(若上述条件均不满足，则打印此句结果)
random的作用是使系统产生随机数，语法——
a=random.randit(x,y),***即生成∈(x,y)的数值代入a中***

**find语句:**

    print(xx.find("a",1,6))
第一个参数查找元素在字符串中位置的下标，默认返回第一次出现的下标；
第二个参数是开始查找的下标位置（默认为零）；
第三个参数是结束查找的下标位置（默认为最后一个）。

**rfind语句:** 

    print(xx.rfind("a",1,6))
第一个参数查找元素在字符串中位置的下标，默认返回第一次出现的下标；
第二个参数是开始查找的下标位置（默认为零）；
第三个参数是结束查找的下标位置（默认为最后一个）。
rfind为从后往前查找字符

**count语法:**

    print(xx.count("a"，1,6)) 
第一个参数为寻找某个元素在字符串出现的次数； 
第二个参数是开始查找的下标位置（默认为零）；
第三个参数是结束查找的下标位置（默认为最后一个）。

**replace语法:**
替换指定字符串片段      

    xx.replace('a','bb',1)
参数1:要替换的字符串片段。
参数2:替换成的字符串片段。
参数3:替换的次数(默认是所有)。   

xx.upper() 即将所有的小写字母换成大写字母。   
xx.lower() 即将所有的大写字母换成小写字母。

**encode函数:**

    xx.encode(encoding='UTF-8',errors='strict')
以encoding指定的编码格式编译字符串。    
如果出错默认报一个valueerror的异常，除非errors指定的是'ignore'或者'replace'

**decode函数:**

    xx.decode(encoding='UTF-8',errors='strict')
以decoding指定的编译格式解析编码

**swith函数:**

    xx.startswith('abc')
判断字符串是否为’abc‘ 开头。

**start/endswith函数:**

    xx.endswith(’txt‘)
判断字符串是否为’txt‘结尾

**isalnum函数:**

    xx.isalnum()
如果字符串中至少有一个字符并且所有字符都是有字符或数字组成则返回True，否则返回false。

**isalpha函数:**

    xx。isalpha()
如果字符串中至少是否都是由字符组成则返回True，否则返回false。

**join函数:**

    s1=','.join('abc')
    print(s1)
以指定字符串作为分隔符，将seq中所有元素(的字符串表示)合并为一个新的字符串

**split语法:**
   
    print(xx.split('a'，2))
第一个参数指根据字符'a'对某个字符串进行分割，得到一个列表。
第二个参数指进行分割的次数。

**(l/r)strip语法:**
s1=xx.lstrip('s')
s2=xx.rstrip('s')
print(s1)
print(s2)
删除字符串中***首尾***相应的字符(默认为删除空格)

**len语法:**
 计算指定字符串/列表的长度————

    s1='fsdasdqwe'
    print(len(s1))

## 列表
 列表的一般形式:

     list1=[1,2,34,5,6,7,8,9,0,'ggb',[1,2,3,4,5,6]]
     print(list[1])
     print(list[10][2])

列表的更新:

     list1=[1,2,34,5,6,7,8,9,0,'ggb',[1,2,3,4,5,6]]
     list1[3]=44
     print(list1)

计算列表长度:

     list1=[1,2,34,5,6,7,8,9,0,'ggb',[1,2,3,4,5,6]]
     print(len(list1)

列表的相加(合并):
    
     list1=[1,2,3,4,5,6]
     list2=[7,8,9,0]
     print(list1+list2)

列表的相乘:

    list1=[1,2,3,4,5,6]
    print(list1*3)

**del语句:**
删除a中的指定值

    a=[1,2,3]
    del a[0]
    print a

**append语法:**
向列表的末位添加元素

    a=[1,2,3]
    a.append(4,5,6,7)
    print(a)

**extend语法:**
向向列表的末位添加元素（推荐使用列表）

a=['杰克','艾斯','高斯',]
a.extend['泰罗','杰斯提斯','雷欧','艾迪']
print(a)

**insert语法:**  
向列表指定位置插入元素

    a=[1,2,3]
    a.insert(1,[4,5,6])
    print(a)
其中，在 'a.insert(1,[4,5,6])'中，第一个参数表示插入的位置，第二个参数表示插入的元素。

**random语法:**  
向列表内填入指定数量的随机数（需要先声明）

     import random
     random_list=[]
     for i in range(10):
         ran=random.randint(1,50)
         random_list.append(ran)
     print(random_list)\
其中，import为引入python库里的random参数;random.randint(1，50)是在1到50之间随即取数

**clear语法:**
清空列表

    a=[1,2,3]
    a.clear()
    print(a)

**remove语法:**
删除第一次出现的指定元素

    a=["qwe","asd","zxc","rtyuiop","fghjkl","vbnm"]
    a.remove("zxc")
    print(a)

**pop语法:**
删除指定位置的元素

    a=["qwe","asd","zxc","rtyuiop","fghjkl","vbnm"]
    a.pop(3)
    print(a)

或指出要移除的元素

    a=["qwe","asd","zxc","rtyuiop","fghjkl","vbnm"]
    print(a.pop(3))

**index语法:**
index函数用于返回所匹配的元素的索引(下标)。

     a=["qwe","asd","zxc","rtyuiop","fghjkl","vbnm"]
     b=a.index('asd',0,5)
     print(b)
该函数的第一个函数表示的是待查找的对象，
第二个参数是查找的起始范围，第三个参数是查找的结束范围。

**reverse语法:**

    a=["qwe","asd","zxc","rtyuiop","fghjkl","vbnm"]
    a.reverse
    print(a)
reverse函数用于将列表反向排列

**extend语法:**
extend函数用于在列表的末尾添加另一个列表。与append函数相比，extend函数可以一次性添加多个元素。
与列表的相加类似。但与列表的相加不同的是，extend是在原列表的基础上形成的列表，而加法是形成了一个新的列表。

**copy语法:**
copy函数用于创建指定列表的副本(即复制品)

    a=["qwe","asd","zxc","rtyuiop","fghjkl","vbnm"]
    b=a.copy()
    print(b)

**sort语法:**
sort函数用于列表的排序(默认升序).
 
    a=["qwe","asd","zxc","rtyuiop","fghjkl","vbnm"]
    a.sort()
    print(a)
不同类型的元素按照ASCll码来排序

**count语法:**
count函数用于统计某个元素在列表中出现的次数。

    a=["qwe","asd","zxc","rtyuiop","fghjkl","vbnm"]
    b=a.count("qwe")
    print(b)

*元组:*
元组使用小括号表示，和列表使用方法类似。元组和列表的唯一区别就是元组的元素是不可变的且元素类型可以不相同。
元组的一般形式————   
a=("hi",66,15,12,[12,13,15])
print(a[])<br>
元祖可以包含一切其他元素，并且用法也与列表相像。 <br>
在print其中，‘[]’表示要寻找下标的元组元素。<br>
元组不能修改，而指定元组中的列表可以修改。

关于元组/列表/字符串的共同操作————        
**len语法+max语法+min语法:**          
len语法用于计算元组/列表/字符串中的元素个数   
max语法用于查找元组/列表/字符串中的最大值   
min语法用于查找元组/列表/字符串中的最小值
    
*集合:*
创建集合:1、a=set().括号中可以为字符串，列表，元组，字典。     
且默认将(列表/元组/字典)里重复的数据去除。

**add语法:**
往集合中添加元素(数字/字符串/元组)       
    
    a ={1,2,3}
    a.add(4,5,6)
**update语法:**
将指定集合合并    

**len函数:**    
输出指定字符串长度

    total=len(s)









































