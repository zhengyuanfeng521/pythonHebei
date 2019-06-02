from matplotlib import pyplot as plt
from pylab import *
import numpy as np
import pandas as pd


class Draw:
    mpl.rcParams['font.sans-serif'] = ['SimHei']

    def sector(self, labels, sizes):
        '''
        :param labels: 每个部分的名称 []
        :param sizes: 每个部分所占比例 []
        :param colors: 每个部分的颜色 []
        :param explode: 每个部分与其他部分之间的间距 ()
        :return:
        '''

        #调节图形大小，宽，高
        # plt.figure(figsize=(12,12))
        plt.figure(figsize=(6, 9))
        # #定义饼状图的标签，标签是列表
        # labels = [u'第一部分',u'第二部分',u'第三部分']
        # #每个标签占多大，会自动去算百分比
        # sizes = [60,30,10]
        # colors = ['red','yellowgreen','lightskyblue']
        # #将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
        # explode = (0.05,0,0)

        colors = ['blue', 'yellowgreen', 'lightskyblue', 'red', 'green', 'yellow', 'red', 'blue', 'green',
                  'yellowgreen', 'pink','yellowgreen', 'lightskyblue', 'red', 'green', 'yellow', 'red', 'blue', 'green',
                  'yellowgreen', 'pink','blue', 'yellowgreen', 'lightskyblue', 'red', 'green', 'yellow', 'red', 'blue', 'green',
                  'yellowgreen', 'pink','yellowgreen', 'lightskyblue', 'red', 'green', 'yellow', 'red', 'blue', 'green',
                  'yellowgreen', 'pink']
        # # 将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
        explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0)
        colors = colors[0:len(labels)]
        explode = explode[0:len(labels)]
        patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,
                                        labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                        startangle = 90,pctdistance = 0.6)

        #labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
        #autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
        #shadow，饼是否有阴影
        #startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
        #pctdistance，百分比的text离圆心的距离
        #patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

        #改变文本的大小
        #方法是把每一个text遍历。调用set_size方法设置它的属性
        for t in l_text:
            t.set_size=(30)
        for t in p_text:
            t.set_size=(20)
        # 设置x，y轴刻度一致，这样饼图才能是圆的
        plt.axis('equal')
        plt.legend()
        plt.show()

    def line_chart(self):

        # 月份
        x1 = ['2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08',
              '2017-09', '2017-10', '2017-11', '2017-12']

        # 体重
        y1 = [86, 85, 84, 80, 75, 70, 70, 74, 78, 70, 74, 80]

        # 设置画布大小
        plt.figure(figsize=(16, 4))

        # 标题
        plt.title("my weight")

        # 数据
        plt.plot(x1, y1, label='weight changes', linewidth=3, color='red', marker='o',
                 markerfacecolor='blue', markersize=10)

        # 横坐标描述
        plt.xlabel('month')

        # 纵坐标描述
        plt.ylabel('weight')

        # 设置数字标签
        for a, b in zip(x1, y1):
            print(a)
            print(b)
            print('---------->>>>>>>>>')
            plt.text(a, b, b, ha='center', va='bottom', fontsize=20)

        plt.legend()
        plt.show()

    def bar_chart(self, name_list, num_list):

        # name_list = ['80-90', '90-100', '100-110', '110-120']
        # num_list = [1.5, 0.6, 7.8, 6]
        plt.xlabel('价格区间/元')
        plt.ylabel('数据/个')
        plt.title('价格区间分布')
        plt.bar(range(len(num_list)), num_list, color='b', tick_label=name_list)
        plt.show()





if __name__ == '__main__':
    draw = Draw()
    #定义饼状图的标签，标签是列表
    # labels = [u'石家庄', u'廊坊', u'衡水']
    # #每个标签占多大，会自动去算百分比
    # sizes = [20, 70, 10]
    # colors = ['blue', 'yellowgreen', 'lightskyblue']
    # #将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    # explode = (0.05,0,0)
    # draw.sector(labels, sizes)
    draw.line_chart()

    # sales_BJ = [10, 20, 30, 40, 50, 60, 70]
    # draw.bar_chart(sales_BJ)



