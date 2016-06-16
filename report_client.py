

#coding=utf-8

import xlsxwriter
import datetime
import pdb

import ods.settings as settings

class Xlsx_Reporter(object):
    """
        xlsx报表生成器
        author : niyoufa
        date : 2016-06-16
        refer : xlsxwriter
    """
    @classmethod
    def get_x_index_list(cls):
        x_index_list = []
        for i in range(97,123):
            for j in range(97,123):
                    x_index_list.append( ( chr(i)+chr(j) ).upper() )
        return x_index_list

    @classmethod
    def get_next_x_index(cls,x_index):
        if len(x_index) == 1 :
            return chr(ord(x_index) + 1)

    def __get_workbook_name(self,*args,**options):
        return options.get("filename",settings.REPORT_PATH + str(datetime.datetime.now()).replace("-","_").\
        replace(" ","_").replace(":","_").replace(".","_")) + ".xlsx"

    def __create_workbook(self,filename,*args,**options):
        return xlsxwriter.Workbook(filename)

    def __create_worksheets(self,workbook,worksheet_names):
        worksheet_dict = {}
        if type(worksheet_names) != type([]):
            raise Exception("param error :work sheet names should be a list")
        elif len(worksheet_names) == 0:
            worksheet_names.append("Sheet1")
        else:
            pass
        for name in worksheet_names :
            worksheet = workbook.add_worksheet(name)
            worksheet_dict[name]= worksheet

        return worksheet_dict

    def __init__(self,*args,**options):
        self.filename = self.__get_workbook_name(*args,**options)
        self.worksheet_names = options.get("worksheet_names",[])
        self.workbook = self.__create_workbook(self.filename)
        self.workbook.worksheet_names = self.worksheet_names
        self.worksheet_dict = self.__create_worksheets(self.workbook,self.workbook.worksheet_names)

    def get_worksheet(self, worksheet_name=None):
        if worksheet_name == None :
            return self.worksheet_dict.values()[0]
        worksheet = self.worksheet_dict.get(worksheet_name, None)
        return worksheet

    def get_worksheets(self,worksheet_names):
        return [self.get_worksheet(name) for name in worksheet_names]

    def get_all_worksheet(self):
        worksheet_names = self.worksheet_names
        worksheets = self.get_worksheets(worksheet_names)
        return worksheets

    def close(self):
        self.workbook.close()

    # 生成xlsx报表
    def report(self,*args,**options):
        X_INDEXS = [chr(i).upper() for i in range(97,123)] + self.get_x_index_list()
        Y_INDEXS = [str(i) for i in range(1,1000)]
        worksheet = options.get("worksheet",None)
        columns = options.get("columns",[])
        data_set = options.get("data_set",[])
        if worksheet == None or  type(columns) != type([]) or type(data_set) != type([]) :
            raise Exception("worksheet can not be None Type")
        else :
            start_index = str(options.get("x_start","A1"))
            if not ( len(start_index) == 2 and start_index[0] in X_INDEXS and start_index[1]  in Y_INDEXS ) : 
                raise Exception("param error :start_index must be right format")
            else :
                start_x_index = start_index[0]
                y_index = start_index[1]
                x_index = start_x_index
                for value in columns:
                    worksheet.write(x_index+y_index,value)
                    x_index = self.get_next_x_index(x_index)

                x_index = start_x_index
                start_y_index = int(start_index[1]) + 1
                y_index = start_y_index
                if len(data_set):
                    if  type(data_set[0]) != type([]) :
                        for value in data_set :
                            worksheet.write(x_index+str(y_index),value)
                            x_index = self.get_next_x_index(x_index)
                    else :
                        for i in data_set :
                            for j in i:
                                worksheet.write(x_index+str(y_index),j)
                                x_index = self.get_next_x_index(x_index)
                            x_index = start_x_index
                            y_index += 1
                            
                else :
                    pass

        # self.close()


    # 生成发货单xlsx报表
    def report_invoice(self):
        pass

if __name__ == "__main__":
    pass
# import ods
# import ods.clients.report_client as report_client
# xlsx_reporter = report_client.Xlsx_Reporter("test")
# worksheet = xlsx_reporter.get_worksheet()
# xlsx_reporter.report(columns=["name"],data_set=[ ["niyoufa"] , ["liuxiaoyan"] ] ,worksheet=worksheet)
# xlsx_reporter.close()
