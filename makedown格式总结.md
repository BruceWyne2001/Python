# Markdown 标题语法:
要创建标题，请在单词或短语前面添加井号 (#) 。# 的数量代表了标题的级别。
# Heading level 1
## Heading level 2
### Heading level 3
# Markdown 段落语法:
要创建段落，请使用空白行将一行或多行文本进行分隔。

I really like using Markdown.

I think I'll use it to format all of my documents from now on.

# Markdown 换行语法:
在一行的末尾添加两个或多个空格，然后按回车键,即可创建一个换行(<br>)。

This is the first line.     
And this is the second line.

# Markdown 强调语法:
通过将文本设置为粗体或斜体来强调其重要性。
## 粗体:
要加粗文本，请在单词或短语的前后各添加两个星号（asterisks）或下划线（underscores）。
如需加粗一个单词或短语的中间部分用以表示强调的话，请在要加粗部分的两侧各添加两个星号（asterisks）。

I just love **bold text**.  
I just love __bold text__.  
## 斜体:
要用斜体显示文本，请在单词或短语前后添加一个星号（asterisk）或下划线（underscore）。
要斜体突出单词的中间部分，请在字母前后各添加一个星号，中间不要带空格。

Italicized text is the *cat's meow*.  
Italicized text is the _cat's meow_.
## 粗体加斜体 :
要同时用粗体和斜体突出显示文本，请在单词或短语的前后各添加三个星号或下划线。
要加粗并用斜体显示单词或短语的中间部分，请在要突出显示的部分前后各添加三个星号，中间不要带空格。
 
This text is ***really important***.   
This text is ___really important___.  
This text is __*really important*__.
# Markdown 引用语法:
要创建块引用，请在段落前添加一个 > 符号。
> Dorothy followed her through many of the beautiful rooms in her castle.
## 多个段落的块引用
块引用可以包含多个段落。为段落之间的空白行添加一个 > 符号。
> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
## 嵌套块引用
块引用可以嵌套。在要嵌套的段落前添加一个 >> 符号。
> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
## 带有其它元素的块引用
块引用可以包含其他 Markdown 格式的元素。并非所有元素都可以使用，你需要进行实验以查看哪些元素有效。
> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.
# Markdown 列表语法
可以将多个条目组织成有序或无序列表。
## 有序列表
要创建有序列表，请在每个列表项前添加数字并紧跟一个英文句点。
数字不必按数学顺序排列，但是列表应当以数字 1 起始。 
1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item
## 无序列表
要创建无序列表，请在每个列表项前面添加破折号 (-)、星号 (*) 或加号 (+) 。
缩进一个或多个列表项可创建嵌套列表。
- First item
- Second item
- Third item
    - Indented item
    - Indented item
- Fourth item
## 在列表中嵌套其他元素
要在保留列表连续性的同时在列表中添加另一种元素，
请将该元素缩进四个空格或一个制表符，如下例所示：
### 段落
*   This is the first list item.
*   Here's the second list item.

    I need to add another paragraph below the second list item.

*   And here's the third list item.
### 引用块
*   This is the first list item.
*   Here's the second list item.

    > A blockquote would look great below the second list item.

*   And here's the third list item.
### 代码块
代码块通常采用四个空格或一个制表符缩进。当它们被放在列表中时， 请将它们缩进八个空格或两个制表符。
1.  Open the file.
2.  Find the following code block on line 21:

        <html>
          <head>
            <title>Test</title>
          </head>

3.  Update the title to match the name of your website.
### 图片
1.  Open the file containing the Linux mascot.
2.  Marvel at its beauty.

    ![Tux, the Linux mascot](图片路径)

3.  Close the file.
# Markdown 代码语法
要将单词或短语表示为代码，请将其包裹在反引号('')中。
At the command prompt, type `nano`.
## 转义反引号.
如果你要表示为代码的单词或短语中包含一个或多个反引号，则可以通过将单词或短语包裹在双反引号中。
``Use `code` in your Markdown file.``
# Markdown 链接语法
链接文本放在中括号内，链接地址放在后面的括号中，链接title可选。
超链接Markdown语法代码：[超链接显示名](超链接地址 "超链接title")  
这是一个链接 [Markdown语法](https://markdown.com.cn)。  
## 给链接增加 Title
链接title是当鼠标悬停在链接上时会出现的文字，
这个title是可选的，它放在圆括号中链接地址后面，跟链接地址之间以空格分隔.  
这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")。  
## 网址和Email地址
使用尖括号可以很方便地把URL或者email地址变成可点击的链接。  
<https://markdown.com.cn>  
<1520182685@qq.com>  
## 带格式化的链接
强调 链接, 在链接语法前后增加星号。 要将链接表示为代码，请在方括号中添加反引号。  
I love supporting the **[EFF](https://eff.org)**.
This is the *[Markdown Guide](https://www.markdownguide.org)*.
See the section on [`code`](#code).
。


