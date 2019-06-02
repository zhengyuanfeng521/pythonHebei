from selenium import webdriver
import time


class Goods:

    def get_goods(self, page):
        mes = []
        driver = webdriver.Chrome()
        url = "https://search.jd.com/Search?keyword=%E6%B2%B3%E5%8C%97%E5%9C%9F%E7%89%B9%E4%BA%A7&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.rem.0.0&wq=%E6%B2%B3%E5%8C%97%E5%9C%9F%E7%89%B9%E4%BA%A7&page="+str(page)+"&s=55&click=0"
        driver.get(url)
        ul = driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul')
        items = driver.find_elements_by_class_name('gl-item')
        print('第'+str(page)+'页')
        print(len(items))
        for item in items:
            price = item.find_element_by_class_name('p-price')
            desc = item.find_element_by_css_selector("[class='p-name p-name-type-2']")
            shop = item.find_element_by_class_name('p-shop')
            commit = item.find_element_by_class_name('p-commit')
            # print('---------------------------------------------------------------------------------------------------------')
            # print(price.text)
            # print(desc.text)
            # print(shop.text)
            # print(commit.text)
            good = {"price": price.text, "desc": desc.text, "shop": shop.text, "commit": commit.text}
            mes.append(good)

            print(good)
        driver.quit()
        time.sleep(1)
        return mes

    def page(self):
        mes = []
        for page in range(1, 167, 2):
            mes += self.get_goods(page)
        return mes


if __name__ == '__main__':
    print("start...")
    goods = Goods()
    goods.get_goods(1)
    # mes = goods.page()
    # print(len(mes))
    # print(mes)

