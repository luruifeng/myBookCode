#coding=utf-8
#@time   :2018/12/30 19:39
#@Author :Keep Learing
#@boke   :www.cnblogs.com/fighter007
#@motto  :Keep Learing

import unittest
from testAPI.Utils.page import  *   #导入Helper工具类
from testAPI.Utils.excles import *  #导入Excels工具类

class Totasks(unittest.TestCase,Helper,Excels):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_register(self):
        '''注册接口'''
        r = self.post(self.readUrl(1),self.readData(1))
        self.assertEqual(r.json()['username'],'jackLu')
        self.Makelog('接口断言：注册接口响应数据检验jackLu')
        self.assertEqual(r.status_code,200)
        self.Makelog('接口断言：注册接口响应状态码检验200')

    def test_login(self):
        '''登录接口'''
        r = self.post(self.readUrl(2),self.readData(2))
        self.assertEqual(r.status_code,200)
        self.Makelog('接口断言：登陆接口响应状态码检验200')
        self.assertEqual(r.json()['username'],'jackLu')
        self.Makelog('接口断言：登陆接口响应数据检验jackLu')

    def test_writeToken(self):
        '''将token写入到Token.md文件中'''
        r = requests.post(self.readUrl(2),self.readData(2))
        with open(self.dirname('Token.md'),'w') as  f:
            self.Makelog('日志跟踪：将token写入到Token.md文件中')
            return f.write(r.json()['token'])

    def read_Token(self):
        '''读取Token.md文件中的token值'''
        with open(self.dirname('Token.md'),'r') as f:
            self.Makelog('日志跟踪：读取Token.md文件中的token')
            return  f.read()

    def setToken(self,rx):
        '''对动态参数token赋值'''
        dinfo = self.readToken(rx)
        self.Makelog('动态参数处理：读取Excel表中的Token值')
        dinfo['token'] = self.read_Token()
        self.Makelog('动态参数处理：对token重新赋值为最新服务器生成的token值')
        return {"Authorization":"Bearer " + dinfo['token']}

    def test_getApiTask(self):
        '''获取所有文章'''
        r = self.get(self.readUrl(3),self.setToken(3))
        self.assertEqual(r.status_code,200)
        self.Makelog('接口断言：获取所有文章响应状态码检验200')

    def test_postApiTasks(self):
        '''创建文章接口'''
        r = self.post(self.readUrl(4),self.readData(4),self.setToken(4))
        self.assertEqual(r.json()['desc'],'接口描述')
        self.Makelog('接口断言：创建文章响应数据断言[接口描述]')
        self.assertEqual(r.status_code, 200)
        self.Makelog('接口断言：创建文章响应状态码检验200')

    def writeTaskId(self):
        '''写入Token到taskID文件中'''
        r = requests.post(self.readUrl(4),self.readData(4),self.setToken(5))
        with open(self.dirname('taskID'),'w') as f:
            f.write(str(r.json()['id']))
            self.Makelog('接口业务：将创建后的文章ID写入到taskID文件中')

    def getTaskID(self):
        '''读取taskID'''
        with open(self.dirname('taskID'),'r') as f:
            self.Makelog('接口业务：读取创建文章后的文章ID')
            return  f.read()

    def test_deleteApiTasks(self):
        '''删除文章接口'''
        r = self.delete(self.readUrl(5) + self.getTaskID(),self.setToken(5))
        self.assertEqual(r.status_code,200)
        self.Makelog('接口断言:删除文章响应状态码检验200')


if __name__ == '__main__':
    unittest.main(verbosity=2)