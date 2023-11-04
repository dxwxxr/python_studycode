# -*- coding: utf-8 -*-
str='  heLlo\n woRld! 哈喽 Hallå' \
    '{name}' \
    ''
str0='ads123一二三'
'''一.大小写转换'''
# #1.首字母大写,其他的全部小写
str1=str.capitalize()
print(str1)
# #2.所有单词首字母大写，其他的全部小写
str2=str.title()
print(str2)
# #3.所有单词大小写转换
str3=str.swapcase()
print(str3)
# #4.所有字母大写转小写
str4=str.lower()
print(str4)
# #5.所有字母大写转换为小写
str5=str.upper()
print(str5)
# #6.字母大写转换为小写
str6=str.casefold()
print(str6)
'''二.填充'''
# #7.字符串在中间，两边以指定宽度和字符填充。当width参数小于字符串长度时，center()方法返回原字符串（即没有产生新的字符串）。
# str7=str.center(30,'-')
# print(str7)
# #8.字符串左对齐，右填充。当width参数小于字符串长度时，ljust()方法返回原字符串（即没有产生新的字符串）。
# str8=str.ljust(30,'*')
# print(str8)
# #9.字符串右对齐，左填充。当width参数小于字符串长度时，rjust()方法返回原字符串（即没有产生新的字符串）。
# str9=str.rjust(30,'-')
# print(str9)
# #10.字符串用零填充。当width参数小于字符串长度时，zfill()方法返回原字符串（即没有产生新的字符串）。
# str10=str.zfill(30)
# print(str10)
'''三.字符串编码'''
#11.对字符串进行编码,默认为utf-8
# str11=str.encode()
# print(str11)
# #12.对字符串进行解码
# str12=str11.decode()
# print(str12)
'''四.字符串查找'''
# #13.返回第一次出现的索引，可设置范围。若无则返回 -1。
# str13=str.find('p',0,len(str))
# print(str13)
# #14.返回最后一次出现的索引，可设置范围。若无则返回 -1。
# str14=str.rfind('p',0,len(str))
# print(str14)
# #15.返回第一次出现的索引，可设置范围。若无则报错。
# str15=str.index('p',0,len(str))
# print(str15)
# #16.返回最后一次出现的索引，可设置范围。若无则报错。
# str16=str.rindex('p',0,len(str))
# print(str16)
'''五.字符串格式化'''
#17.用于格式化字符串,以大括号{}来标明被替换的字符串。
#以{}填充，通过索引填充，通过变量名填充，通过类访问对象属性填充，对参数部分进行引用，对数字进行处理，对列表进行引用对字典的值进行引用。
# str17=str.format(name='aaa')
# print(str17)
#18.适用于字符串格式中可变数据参数来源于字典等映射关系数据时才可以使用。
# dict={'name':'jock'}
# str18=str.format_map(dict)
# print(str18)
'''六。解决判断问题'''
'''查找'''
# #19.判断字符串是否以指定字符串结尾
# str19=str.endswith(']')
# print(str19)
# #20.判断字符串是否以指定字符串结尾
# str20=str.startswith('h')
# print(str20)
'''大小写，特使字符,标识符'''
# #21.检测判断字符串中所有单词的首字母是否为大写，且其它字母是否为小写
# str21=str.istitle()
# print(str21)
# #22.判断字符串中是否有打印后不可见的内容。如：\n \t  等字符。
# str22=str.isprintable()
# print(str22)
# #23. 检测字符串是否只由空格组成。若字符串中只包含空格，则返回 True
# str23=str.isspace()
# print(str23)
# #24.检测字符串中的字母是否全由小写字母组成。（字符串中可包含非字母字符）
# str24=str.islower()
# print(str24)
# #25.检测字符串中的字母是否全由大写字母组成。（字符串中可包含非字母字符）
# str25=str.isupper()
# print(str25)
'''判断字母数字'''
# #26.判断str是否是有效的标识符。
# str26=str.isidentifier()
# print(str26)
# '''字母数字'''
# #27.检测字符串是否只由字母和数字组成。
# str27=str0.isalnum()
# print(str27)
# #28.检测字符串是否只由字母组成。
# str28=str0.isalpha()
# print(str28)
# #29.检测字符串是否只由十进制数字组成。
# str29=str0.isdecimal()
# print(str29)
# #30.检测字符串是否只由数字组成.字符串中至少有一个字符且所有字符都是数字。能判断“①”，不能判断中文数字。
# str30=str0.isdigit()
# print(str30)
# #31.测字符串是否只由数字组成。这种方法是只适用于unicode对象。
# str31=str0.isnumeric()
# print(str31)
'''字符串切片'''
# #32.该函数的作用是去除字符串开头和结尾处指定的字符，不会去除字符串中间对应的字符，默认去除空格或换行符。
# str32=str.strip()
# print(str32)
# #33.lstrip() 方法用于截掉字符串左边的空格或指定字符。
# str33=str.lstrip()
# print(str33)
# # 34.删除 str 字符串末尾的指定字符（默认为空格）
# str34=str.lstrip()
# print(str34)
'''字符串加密解密'''
#35.制作翻译表，删除表，常与translate()函数连用。加密根据Unicode编码。前面的不能重复，否则会被覆盖。
# str35=str.maketrans('aav','234')
# print(str35)
# #36.过滤(删除)，翻译字符串。即根据maketrans()函数给出的字符映射转换表来转换字符串中的字符。
# str36=str.translate(str35)
# print(str36)
'''分割字符串'''
# #37.根据指定的分隔符(sep)将字符串进行分割。从字符串左边开始索引分隔符sep,索引到则停止索引。返回值：(head, sep, tail)  返回一个三元元组，head:分隔符sep前的字符串，sep:分隔符本身，tail:分隔符sep后的字符串。如果字符串包含指定的分隔符sep，则返回一个三元元组，第一个为分隔符sep左边的子字符串，第二个为分隔符sep本身，第三个为分隔符sep右边的子字符串。如果字符串不包含指定的分隔符sep,仍然返回一个三元元组，第一个元素为字符串本身，第二第三个元素为空字符串.
# str37=str.partition('\n')
# print(str37)
# #38.根据指定的分隔符(sep)将字符串进行分割。从字符串右边(末尾)开始索引分隔符sep,索引到则停止索引。
# str38=str.rpartition("l")
# print(str38)
# #39.拆分字符串。通过指定分隔符sep对字符串进行分割，并返回分割后的字符串列表。
# str39=str.split('l',maxsplit=1)
# print(str39)
# #40.拆分字符串。通过指定分隔符sep对字符串进行分割，并返回分割后的字符串列表,类似于split()函数，只不过 rsplit()函数是从字符串右边(末尾)开始分割。。
# str40=str.rsplit('l',maxsplit=2)
# print(str40)
# #41.按照('\n', '\r', \r\n'等)分隔，返回一个包含各行作为元素的列表，默认不包含换行符。keepends -- 在输出结果里是否去掉行界符('\r', '\r\n', \n'等)，默认为 False，不包含行界符，如果为 True，则保留行界符。
# str41=str.splitlines(keepends=False)
# print(str41)
'''新增字符串'''
# #42.将iterable变量的每一个元素后增加一个str字符串。sep——分隔符。可以为空。iterable—— 要连接的变量 ，可以是 字符串，元组，字典，列表等。
# list=['a','b','c']
# str42=','.join(list)
# print(str42)
'''字符串替换'''
# #43.把str.中的 old 替换成 new,如果 count 指定，则替换不超过 count次.。old —— 将被替换的子字符串。new —— 新子字符串，用于替换old子字符串。,count —— 替换的次数，默认全部替换。
# str43=str.replace('l','#',2)
# print(str43)
# # #44.将字符串S中的 \t 替换为一定数量的空格。默认tabsize中N=8
# str44=str.expandtabs()
# print(str44)
# '''统计次数'''
# #45.统计字符串里某个字符出现的次数。可以选择字符串索引的起始位置和结束位置。
# str45=str.count('l')
# print(str45)