#coding=utf-8
#@time   :2019/1/1 17:42
#@Author :Keep Learing
#@boke   :www.cnblogs.com/fighter007
#@motto  :Keep Learing


import xlrd,json

class Excels(object):

    '''构造 Excel 工具类'''

    def readExcelData(self,rowx):
        '''读取rowx行数'''
        book  = xlrd.open_workbook(r'D:\project\testAPI\Data\data.xlsx')
        table = book.sheet_by_index(0)
        return table.row_values(rowx)

    def readUrl(self,rowx):
        '''读取接口地址'''
        return self.readExcelData(rowx)[0]

    def readData(self,rowx):
        '''读取请求参数'''
        return json.loads(self.readExcelData(rowx)[1])

    def readToken(self,rowx):
        '''读取Token'''
        return json.loads(self.readExcelData(rowx)[2])


# e = Excels()
# print(e.readUrl(1))
# print(e.readData(1),type(e.readData(1)))
#
#





