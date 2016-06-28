#coding=utf8
#author = yxp
"""
    配置elasticsearchp2.2
    jdk1.8
    本配置文件以 路径，loging为主
"""

ES_PATH = "http://127.0.0.1:9200"


#ES 定义index字段  
"""
    analyzed 使用分词器
    analyzer  分词器类型
"""
ES_FIELD_MAPPING = {
    "id" :
        {"index":"no","type":u'integer'},
    "sha1" :
        {"index":"analyzed","type":u'string','store': 'yes'},
    #标题
    "title":
        {"index":"analyzed","type":u'string','store': 'yes',},
    #作者
    "author" :
        {"index":"analyzed","type":u'string','store': 'yes',},
    #创建时间
    "creation_time" :
        {"index":"analyzed","type":u'date'},
    #是否允许主动传播
    "broadcast":
        {"index":"no","type":u'boolean'},
    #参与人数
    "nb_participants" :
        {"index":"analyzed","type":u'integer'},
    #插件类型: 调查问卷，监督举报等
    "plugin" :
        {"index":"analyzed","type":u'string'},
    #功能类别标签：排行榜，求安慰等
    "func_tags":
        {"index":"analyzed","type":u'string',},
    #行业大标签 list 
    "topic_tags" :
        {"index":"analyzed","type":'string','store': 'yes'},
    #兴趣小标签 list
    "interest_tag":
        {"index":"analyzed","type":'string','store': 'yes'},
    #描述
    "description" :
        {"index":"no","type":u'string'},
    #版本
    "_version_":
        {"index":"analyzed","type":u'long'},
    #地理位置,经纬度 [经度,纬度]
    "geo":
        {"index":"analyzed","type":u'geo_point','store': 'yes',},
    #发布活动时的参与者限制条件列表
    "limits" :
        {"index":"analyzed","type":u'string'},
    #参与类型 0 :所有用户 1:联系人
    "participant_type" :
        {"index":"no","type":u'integer'},
    #图片列表
    "image_sha1s":
        {"index":"no","type":u'string'},
    #分享设置 1:可以分享 0:不可以分享
    "can_be_shared" :
        {"index":"no","type":u'integer'},
    #分享次数
    "nb_shares" :
        {"index":"analyzed","type":u'integer'},
    #多少人已经完成任务或已签到
    "nb_completes":
        {"index":"analyzed","type":u'integer'},
    #根据坐标反解析出的地理位置信息，比如海淀区学清路38号
    "loc" :
        {"index":"analyzed","type":u'string'},
    #城市
    "city" :
        {"index":"analyzed","type":u'string'},
    #百度地图对应的城市编码
    "city_code":
        {"index":"analyzed","type":u'integer'},
    #发起人类型：0表示以个人名义发起，1表示以公司名义发起
    "organizer_type" :
        {"index":"analyzed","type":u'integer'},
     #是否有红包, 缺省免费没有
    "has_bonus" :
        {"index":"no","type":u'boolean'},
    #此项投票或是任务的红包总金额
    "total_amount":
        {"index":"analyzed","type":u'float'},
    #红包派发给多少人
    "nb_rewarded_people":
        {"index":"analyzed","type":u'integer'},
    #红包派发类型: 0:最先参与的若干个人；1:根据结果审批的若干个人；
    "bonus_type" :
        {"index":"analyzed","type":u'integer'},
    #红包是否已经派发0 :未派发 1:已派发
    "is_bonus_paid":
        {"index":"analyzed","type":u'integer',},
    #红包发放是否已经结算：0 :未结算 1:已结算
    "is_account" :
        {"index":"analyzed","type":u'integer',},
    "creator_sha1" :
        {"index":"analyzed","type":u'string',},
    "sub_type" :
        {"index":"analyzed","type":u'integer',},
    "status" :
        {"index":"analyzed","type":u'integer',},
}

#conn.put_mapping("man", {'properties':mapping}, ["human"]) 相当于create table操作

import datetime
creation_time = datetime.datetime(1992,8,6)
example_data = {
    "id" :892222,
    "sha1" :'afafwqfwqfwqasdfsdadfdfdffdaesadfrqwer',
    "title":'panpan',
    "author" :"yxp",
    "creation_time" :creation_time,
    "broadcast":True,
    "nb_participants" :123,
    "plugin" :"sdaf",
    "func_tags":'asdf',
    "topic_tags" :['加拿大','朝鲜'],
    "interest_tag":['美国','中国','英国','日本','俄国','新西兰','爱尔兰'],
    "description":"asdfsda",
    "_version_":1323,
    #地理位置,经纬度 [经度,纬度]
    "geo":[11,12],
    #发布活动时的参与者限制条件列表
    "limits" :'121313',
    #参与类型 0 :所有用户 1:联系人
    "participant_type" :2,
    #图片列表
    "image_sha1s":'13321',
    #分享设置 1:可以分享 0:不可以分享
    "can_be_shared" :1,
    #分享次数
    "nb_shares" :544,
    #多少人已经完成任务或已签到
    "nb_completes":46546,
    #根据坐标反解析出的地理位置信息，比如海淀区学清路38号
    "loc" :'asdfsad',
    #城市
    "city" :'南京',
    #百度地图对应的城市编码
    "city_code":23,
    #发起人类型：0表示以个人名义发起，1表示以公司名义发起
    "organizer_type" :2,
     #是否有红包, 缺省免费没有
    "has_bonus" :False,
    #此项投票或是任务的红包总金额
    "total_amount":1213.213,
    #红包派发给多少人
    "nb_rewarded_people":56,
    #红包派发类型: 0:最先参与的若干个人；1:根据结果审批的若干个人；
    "bonus_type" :2,
    #红包是否已经派发0 :未派发 1:已派发
    "is_bonus_paid":200,
    #红包发放是否已经结算：0 :未结算 1:已结算
    "is_account" :100,
    #对象类型: 
    "sub_type":0,
    #用户user_sha1
    "creator_sha1":"123232"

}

# coding=utf-8
import  datetime, time, json, pdb
import pyes
from pyes import *
from pyes.queryset import generate_model
from  es_settings  import *
import cPickle as pickle
import logging
from xieli.models import * 

#连接es服务器
def _connect_index():
    conn = pyes.ES(ES_PATH, timeout=200.0)
    return conn

#创建index索引表
def create_index(name):
    conn = _connect_index()
    conn.indices.create_index(name)
    conn.indices.put_mapping("CommonObject", {'properties':ES_FIELD_MAPPING}, [name])

#删除index
def delete_index(name):
    conn = _connect_index()
    conn.indices.delete_index(name)

#向es插入数据
def insert_into_es(params,index_name,index_type):
    #参数矫正
    conn = _connect_index()
    conn.index(params,index_name,index_type)

#获取es数据，形成类似django model对象
def get_index_model(database,table):
    return generate_model(database, table,es_url=ES_PATH)

#获取所有相关的记录
def march_query_alltag(field,query):
    conn = _connect_index()
    b = MatchQuery(field,query)
    return [i for i in conn.search(query =b)]

#must + should
def march_query_tag(field,query,sub_type):
    conn = _connect_index()
    must = pyes.TermQuery("sub_type",sub_type)
    should = pyes.MatchQuery(field,query)
    query = pyes.BoolQuery(must = must ,should = should)
    return [i for i in conn.search(query =query)]

#获取协力对象列表
def get_object_list(user_sha1,sub_type,tag_name,query_time): 
    """ 
        备注 : 协力对象查询
        请求参数 : 
        user_sha1 用户sha1 
        sub_type 对象类型 
        tag_name : 标签名称 可以为空
        query_time : 查询时间
        返回参数 : 
        obj_list : ((user_sha1,obj_sha1),)          
        例如 : ( (u'acdd6c3b14284cae21cd38feabf53b8151111f6a', u'2084610fe24c26d131bad8a91563583435c55c13'), ) 
        说明 : 
        user_sha1 : 用户sha1
        obj_sha1 : 协力对象sha1
    """

    #step1: 从user表，taggroup表获取 tag
    # commobj = xieli_recommend(user_sha1,1,sub_type)
    if int(sub_type) == 0:
        commobj = get_index_model("teamup","CommonObject").objects.exclude(creator_sha1 = user_sha1).all()
    else:
        commobj = get_index_model("teamup","CommonObject").objects.filter(sub_type = sub_type).exclude(creator_sha1 = user_sha1)
    results_list = []
    for obj in commobj:
        results_list.append(obj.sha1)

    return results_list

#查询(移动端进行的全局查询)
def search_query(query):
    conn = _connect_index()
    title_object = MatchQuery("title",query)
    description_object = MatchQuery("description",query)
    title_object_list =  [i for i in conn.search(query =title_object)]
    description_object_list =  [i for i in conn.search(query =description_object)]
    for title in title_object_list:
        if title not in description_object_list:
            description_object_list.append(title)

    results_list = []
    for obj in description_object_list:
        results_list.append((obj.creator_sha1,obj.sha1))
        print obj.title
        print obj.sha1
    return tuple(results_list)


 # 限定时间内的es数据
def  _index_time(date_range, query):
    if type(date_range) == type(-1) and date_range != -1:
        start_date = last_time()
        print start_date
        #start_da = datetime.datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ").date()
        start_da = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = (start_da + datetime.timedelta(days=date_range)).strftime('%Y-%m-%d')
        print end_date
        # query.add_must(pyes.RangeQuery(pyes.ESRange('pubtime',from_value=start_date, to_value=end_date)))
        query.add_must(pyes.RangeQuery(pyes.ESRange('datestring', from_value=start_date, to_value=end_date)))
        return query, end_date
    else:
        print '请输入int类型时间间隔'

# 利用pickle保存上一次获取新闻时间
def last_time():
    input = open('news_time.txt', 'rb')
    try:
        #读取上一次时间
        last_time = pickle.load(input)
    except Exception, e:
        #读取失败，就从settings中的start 时间开始
        print e
        last_time = start_day
    input.close()
    return last_time
    
# 配置文件
def get_log():
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='recommend_xieli_yxp.log',
                    filemode='a')  
    return logging