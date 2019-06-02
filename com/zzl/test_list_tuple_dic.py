import numpy as np
import re
# # list
# list1 = ['physics', 'chemistry', 1997, 2000]
# print(list1)
# print(list1[1])
#
# list1.append('google')
# print(list1)
#
# del list1[4]
# print(list1)
#
# list2 = []
# list2.append('123')
# print(list2)
#
# '''
#     其他的简单操作
#     len()
#     +
#     *
#     3 in [1,2,3]
#     for x in [1,2,3]:
#         print(x)

# touple

# print(sum([2,3]))

# num = 58/1379
# print(num)
# print(round(num * 100))


# colors = ['blue', 'yellowgreen', 'lightskyblue', 'red', 'green', 'yellow', 'red', 'blue', 'green',
#                   'yellowgreen', 'blue']
# # # 将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
# explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
# temp = [23, 23]
# print(len(temp))
# print(colors[0:len(temp)])
# print(explode[0:len(temp)])

# print(np.arange(7))

# print(re.match('www', 'www.runoob.com').span())
# print(re.match('com', 'www.runoob.com'))
# string = 'jfkdsljf'
# print(type(string))
# print(string.startswith('jf', 0, len(string)))

str = '2金风科技来看'
if '人拼' in str:
    print('在')
else:
    print('不在')
