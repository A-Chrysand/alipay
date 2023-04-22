from random import randint
import time


def getOrderId() -> str:
	'''
	生成订单号，由时间戳和10位随机数字组成
	:return: 返回随机订单号(str)
	'''
	timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
	# 生成len长度的随机字符串
	s = ""
	for i in range(10):
		s += str(randint(0, 9))
	return timestamp + s


def params_filter(param):
	'''
	参数排序和筛选
	:param param: 待排序数据(dict)
	:return: 排序后的数据(str)
	'''
	keys_d = param.keys()
	keys = [key for key in keys_d]
	keys.sort()
	prestr = ''
	for key in keys:
		if not param[key]:
			continue
		prestr += "{0}={1}&".format(key, param[key])
	return prestr[0:-1]
