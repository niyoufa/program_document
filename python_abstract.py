class AbstractReportCreator :
	"""
	创建各种报表的抽象类,在其子类中完成创建报表的具体工作
	"""
	__metaclass__ = ABCMeta

	#写入报表样式
	@abstractmethod
	def write_report_format_info(self,workbook):
		pass

	#写入报表context
	@abstractmethod
	def write_report_context_info(self,worksheet,format_list):
		pass

	#写入报表数据
	@abstractmethod
	def  write_report_info(self,worksheet,location,tag,unit,user_id):
		pass

	#写入报表的图表
	@abstractmethod
	def write_report_dash(self,workbook,unit,location,tag,worksheet):
		pass

	#导入自动计算函数定义
	@abstractmethod
	def write_report_func_define(self,worksheet,format_list,user_id,location,data):
		pass

	#统筹创建报表过程
	@abstractmethod
	def make_report_xlsx(self,location,tag,unit,*args,**kw):
		pass