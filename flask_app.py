import json

from flask import Flask, request, redirect, make_response

import setting

from api.utils import getOrderId
from api.alipay import place_order, notify_verify

app = Flask(__name__)


@app.route('/', methods=['get'])
def helloworld():
	return '''
	<h1>helloworld</h1>
	<a href="/api">点我创建订单</a><br>
	当前为：''' + setting.item_name + ' | ' + str(setting.money) + '元' + \
                          '<br><br>商品价格等信息可到setting.py修改'


@app.route("/api", methods=["GET"])
def alipay():
	mon = request.args.get("money")
	if not mon:
		mon = setting.money
		url = place_order(
		    orderId=getOrderId(),  #这个orderid可以自己用其他方法生成，例如调用实际项目数据库数据再计算什么的
		    money=float(mon),
		    orderTitle=setting.item_name,
		    return_url="http:" + setting.host + ':' + str(setting.port) +
		    setting.callback)
	print(url)
	return redirect(url, code=302)


@app.route(setting.callback)
def callback():
	if request.method == 'POST':
		param = request.form.to_dict()
	elif request.method == 'GET':
		param = request.args.to_dict()
	else:
		return "error"
	print(param)
	re = notify_verify(param)  #<bool>True/False 参数是否校验成功
	print('收到付款' + param.get('total_amount') + '元，完成订单' +
	      param.get('out_trade_no'))
	return make_response("success<br>notify_verify(param)=" + json.dumps(re) +
	                     '<br>param=' + json.dumps(param))


app.run(host=setting.host, port=setting.port, debug=setting.debug)
