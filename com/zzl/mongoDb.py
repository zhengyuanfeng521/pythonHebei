from pymongo import MongoClient


class MongoDBUtils:
    conn = MongoClient('118.24.194.103', 27017)
    # db = conn.mydb  # 获取数据库 没有回创建
    # my_set = db.test_set # 获取set 没有会创建

    def insert_data(self, data, db_name, set_name):
        set = self.conn.db_name.set_name
        set.insert(data)

    def select(self,db_name, set_name):
        # for i in self.conn.db_name.set_name.find():
        #     print(i)
        return self.conn.db_name.set_name.find()

if __name__ == '__main__':
    mutils = MongoDBUtils()
    # mutils.insert_data({'test': 'test data'}, 'db_test', 'set_test')
    items = mutils.select('db_test', 'set_test')


