from get_place_name import GetPlace
from test import Goods
from mongoDb import MongoDBUtils
from test_draw import Draw


class Main:
    get_place = GetPlace()

    def store_goods(self):
        goods = Goods()
        mes = goods.page()
        mongoDB = MongoDBUtils()
        mongoDB.insert_data(mes, 'jd', 'goods')
        print('store finished')

    def select_goods(self):
        mongoDB = MongoDBUtils()
        return mongoDB.select('jd', 'goods')

    def get_shi(self):
        return self.get_place.get_shi()

    def get_xian(self):
        return self.get_place.get_xian()

    def get_shi_sector(self):
        shi_goods_dict = {'承德': 58, '邢台': 26, '张家口': 139, '衡水': 42, '沧州': 118, '唐山': 250, '保定': 451, '廊坊': 24, '秦皇岛': 7,
                          '石家庄': 106,
                          '邯郸': 158}
        sum1 = sum(shi_goods_dict.values())
        print(sum1)
        labels = shi_goods_dict.keys()
        proportion = []
        for i in shi_goods_dict.values():
            proportion.append(round((i / sum1) * 100))
        print(proportion)
        draw = Draw()

        draw.sector(labels, proportion)

    def get_price_bar_chart(self):
        draw = Draw()
        prices = []
        name_list = ['0-40', '40-80', '80-120', '120-160', '160-200', '200-240', '240-280', '280-320']

        name_num_dict = {}
        # 建立 name_num_dict的 dict
        for i in name_list:
            name_num_dict[i] = 0
        print('建立之后')
        print(name_num_dict)

        for good in main.select_goods():
            price = good['prize']

            if '人拼' in price:
                continue
            elif '\n' in price:
                continue
            else:
                # print(price[1:len(price)])
                price = float(price[1:len(price)])
                prices.append(price)

                if price >= 0 and price < 40:
                    name_num_dict['0-40'] = name_num_dict['0-40'] + 1
                elif price >= 40 and price < 80:
                    name_num_dict['40-80'] = name_num_dict['40-80'] + 1
                elif price >= 80 and price < 120:
                    name_num_dict['80-120'] = name_num_dict['80-120'] + 1
                elif price >= 120 and price < 160:
                    name_num_dict['120-160'] = name_num_dict['120-160'] + 1
                elif price >= 160 and price < 200:
                    name_num_dict['160-200'] = name_num_dict['160-200'] + 1
                elif price >= 200 and price < 240:
                    name_num_dict['200-240'] = name_num_dict['200-240'] + 1
                elif price >= 240 and price < 280:
                    name_num_dict['240-280'] = name_num_dict['240-280'] + 1
                elif price >= 280 and price < 320:
                    name_num_dict['280-320'] = name_num_dict['280-320'] + 1
        print('筛选之后')
        print(name_num_dict)

        num_list = name_num_dict.values()
        draw.bar_chart(name_list, num_list)




if __name__ == '__main__':
    # get_place = GetPlace()
    # shi = get_place.get_shi()
    # xian = get_place.get_xian()
    # print('---------------------------->')
    # print('河北的市')
    # print(shi)
    # print('河北市中包含的县')
    # print(xian)

    main = Main()
    shi = main.get_shi()

    shi_goods_dict = {}
    # print(shi['河北'])


    # 创建 每个市中有多少 特产的dict
    for shi_name in shi['河北']:
        shi_goods_dict[shi_name] = 0
    # print(shi_goods_dict)
    # print(type(shi_goods_dict[shi_name]))


    # # 配置 市名的字典中的数据
    # for shi_name in shi['河北']:
    #     for good in main.select_goods():
    #         if shi_name in good['desc']:
    #            shi_goods_dict[shi_name] =  shi_goods_dict[shi_name]+1
    #
    # print(shi_goods_dict)

    # 县的设置
    xian_goods_dict = {}
    xian = main.get_xian()
    print('--------------------->县')
    print(xian['保定'])
    # 创建 保定 县中字典
    for xian_name in xian['保定']:
        if xian_name == '唐':
            xian_goods_dict['唐县'] = 0
        elif xian_name == '易':
            xian_goods_dict['易县'] = 0
        elif xian_name == '雄':
            xian_goods_dict['雄县'] = 0
        elif xian_name == '蠡':
            xian_goods_dict['蠡县'] = 0
        else:
            xian_goods_dict[xian_name] = 0

    # # 配置 县名的字典中的数据
    # for xian_name in xian_goods_dict.keys():
    #     for good in main.select_goods():
    #         if xian_name in good['desc']:
    #            xian_goods_dict[xian_name] = xian_goods_dict[xian_name]+1

    print("xian_goods_dict")
    xian_goods_dict = {'清苑': 0, '唐县': 17, '安新': 14, '雄县': 0, '保定白沟新': 0, '定兴': 1, '涿州': 0, '满城': 0, '定州': 29, '竞秀': 0, '蠡县': 10, '望都': 7,
     '顺平': 4, '曲阳': 57, '高碑店': 33, '涞水': 0, '博野': 5, '阜平': 1, '徐水': 9, '莲池': 0, '容城': 0, '高阳': 0, '涞源': 3, '易县': 5,
     '安国': 5, '保定高新技术产业开发': 0}

    print(xian_goods_dict)
    print(xian_goods_dict.values())
    sum1 = sum(xian_goods_dict.values())
    print('sum1 = ')
    print(sum1)
    labels = xian_goods_dict.keys()
    proportion = []
    for i in xian_goods_dict.values():
        proportion.append(round((i / sum1) * 100))
    print("**************************************************************")
    print(labels)
    print(proportion)
    draw = Draw()
    #
    draw.sector(labels, proportion)


    '''扇形图的分类'''
    # shi_goods_dict = {'承德': 58, '邢台': 26, '张家口': 139, '衡水': 42, '沧州': 118, '唐山': 250, '保定': 451, '廊坊': 24, '秦皇岛': 7, '石家庄': 106,
    #  '邯郸': 158}
    # sum = sum(shi_goods_dict.values())
    # print(sum)
    # labels = shi_goods_dict.keys()
    # proportion = []
    # for i in shi_goods_dict.values():
    #     proportion.append(round((i/sum) * 100))
    # print(proportion)
    draw = Draw()

    # draw.sector(labels, proportion)
    #
    # main.get_shi_sector()



    '''价格的设置'''
    #
    # draw = Draw()
    # prices = []
    # name_list = ['0-40', '40-80', '80-120', '120-160', '160-200', '200-240', '240-280', '280-320']
    #
    # name_num_dict = {}
    # # 建立 name_num_dict的 dict
    # for i in name_list:
    #     name_num_dict[i] = 0
    # print('建立之后')
    # print(name_num_dict)
    #
    #
    # for good in main.select_goods():
    #     price = good['prize']
    #
    #     if '人拼' in price:
    #         continue
    #     elif '\n' in price:
    #         continue
    #     else:
    #         # print(price[1:len(price)])
    #         price = float(price[1:len(price)])
    #         prices.append(price)
    #
    #         if price>=0 and price <40:
    #             name_num_dict['0-40'] = name_num_dict['0-40'] + 1
    #         elif price>=40 and price <80:
    #             name_num_dict['40-80'] = name_num_dict['40-80'] + 1
    #         elif price>=80 and price <120:
    #             name_num_dict['80-120'] = name_num_dict['80-120'] + 1
    #         elif price >= 120 and price < 160:
    #             name_num_dict['120-160'] = name_num_dict['120-160'] + 1
    #         elif price >= 160 and price < 200:
    #             name_num_dict['160-200'] = name_num_dict['160-200'] + 1
    #         elif price >= 200 and price < 240:
    #             name_num_dict['200-240'] = name_num_dict['200-240'] + 1
    #         elif price >= 240 and price < 280:
    #             name_num_dict['240-280'] = name_num_dict['240-280'] + 1
    #         elif price >= 280 and price < 320:
    #             name_num_dict['280-320'] = name_num_dict['280-320'] + 1
    # print('筛选之后')
    # print(name_num_dict)
    #
    # num_list = name_num_dict.values()
    # draw.bar_chart(name_list, num_list)

    # main.get_price_bar_chart()


    # 最大价格 最小价格 平均价格的交代
    # sum_price = 0
    # count_price = 0
    # max_price = 0
    # min_price = 0
    # for good in main.select_goods():
    #     price = good['prize']
    #     if '人拼' in price:
    #         continue
    #     elif '\n' in price:
    #         continue
    #     else:
    #         temp_price = float(price[1:len(price)])
    #         sum_price = sum_price + temp_price
    #         count_price = count_price + 1
    #         if max_price < temp_price:
    #             max_price = temp_price
    #         if min_price > temp_price:
    #             min_price = temp_price
    #
    # sum_avg = round(sum_price / count_price)
    # print('平均价格')
    # print(sum_avg)
    # print('最大价格')
    # print(max_price)
    # print('最小价格')
    # print(min_price)












