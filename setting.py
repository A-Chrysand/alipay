# server
host = '127.0.0.1'
port = 5000
debug = True

# order
item_name = 'test商品名称'  # 商品名称
shop_name = 'testXX商城'  # 商户名称/收款方账号
money = 66  # 交易金额 ,你可以通过访问loaclhost:%port%?money=%money%来自定义金额

# 商户信息，以下内容可以在https://open.alipay.com/develop/sandbox/app找到
# 复制你的沙箱账号到这里
app_id = "2021000122679681"

method = "alipay.trade.page.pay"  # 如果想使用网页显示二维码，手机支付宝扫码再支付，就用这个
# method = "alipay.trade.wap.pay" # 如果想网页直接提示“是否打开手机支付宝付款”那就用这个
# 支付宝网关地址
gateway = "https://openapi.alipaydev.com/gateway.do?"
# 授权回调地址
# 如果你在支付宝沙箱应用里设置的是http://192.168.123.104:5000/callback/，那只需写pathname（就是不要前面http://的那一截）
callback = '/callback/'

format = "json"
charset = "utf-8"
sign_type = "RSA2"
version = "1.0"
notify_url = ""

# app私钥，选择非JAVA语言，复制粘贴到↓文件中，记住要保留首行和末行的开始结束标识
app_private_key = open('keys/app_private_key.txt', "r").read()
# app公钥，暂时没什么用
app_public_key = open('keys/app_public_key.txt', 'r').read()
# 支付宝公钥，直接复制到↓文件
alipay_public_key = open('keys/alipay_public_key.txt', 'r').read()
