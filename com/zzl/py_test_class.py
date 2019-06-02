
class Test_Class:
    '''测试python的类'''
    def print123(self):
        print(123)









if __name__ == '__main__':
    # print('hello')
    # tc = Test_Class()
    # tc.print123()

    # # 列表的使用
    # t = ('保定', '石家庄', '张家口', '邢台', '衡水', '承德', '邯郸', '廊坊', '唐山', '秦皇岛', '沧州')
    # print(t)
    list = ['保定', '石家庄', '张家口', '邢台', '衡水', '承德', '邯郸', '廊坊', '唐山', '秦皇岛', '沧州']
    print(list)
    place = '保定'
    if place in list:
        print(place)

    hb = {'河北': list}
    print(hb)
