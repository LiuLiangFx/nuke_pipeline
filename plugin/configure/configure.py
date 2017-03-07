# -*- coding:utf-8 -*-
import os
from collections import OrderedDict
import connectMongo

########################
#
#   配置文件设置
#
########################

# 项目素材根目录
source_root_path = "Z:/Plates/"

# 制作人员列表
artists_list = [u"侯世鹏", u"郭伟", u"常亚茹"]

# mongodb的ip及端口设置
mongodb_ip = "10.0.0.117"
mongodb_port = 27017

# 连接 daliy 数据库
connect_mongo = connectMongo.connect_mongo()

# 连接 progress 数据库
connect_mongo_progress = connectMongo.connect_mongo_progress()

# lic 存放位置
lic_path = "D:/pipeline.lic"

# daliy 数据库内容
db_dataName = OrderedDict(
	[(u"项目名", u"project"), (u"镜头名", u"shot_name"), (u"文件名", u"file_name"), (u"制作人员", u"user_name"),
	 (u"帧数", u"frame_len"), (u"是否通过", u"pass_value"), (u"反馈", u"feed_back"), (u"日期", u"date")])

# grader 数据库内容
db_progress_dataName = OrderedDict(
	[(u"项目名", u"project"), (u"镜头名", u"shot_name"), (u"帧数", u"frame_len"), (u"级别", u"grade"), (u"分配人员", u"artist"),
	 (u"制作人员", u"user_name"), (u"内部审核", u"pass_value"), (u"客户反馈", u"client_feed_back"), (u"阶段完成日期", u"date")])

# TODO: 或许需要一个 artist 和 user 的键值对