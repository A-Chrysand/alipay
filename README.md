# Flask的支付宝API项目Demo
## 项目介绍
此项目fork自[Github: panyunsuo/alipay](https://github.com/panyunsuo/alipay)，进行修改
## 测试Demo
1. 安装依赖
```shell
# 依赖包不一定准确，请自行根据实际情况调整
pip install pyopenssl flask
```
2. 运行项目
```shell
py flask_app.py
```
3. 浏览器访问```http://localhost:5000```查看项目

## 项目介绍
%project_root%  
&ensp;|--setting.py   #应用设置  
&ensp;|--flask_app.py  #flask入口  
&ensp;|--README.md  
&ensp;|--/keys   
&ensp;|&emsp;&emsp;|--alipay_public_key.txt  #存放支付宝公钥（可在支付宝沙箱内找到）  
&ensp;|&emsp;&emsp;|--app_private_key.txt  #存放应用私钥（可在支付宝沙箱内找到）  
&ensp;|&emsp;&emsp;|--app_public_key.txt  #存放应用公钥（可在支付宝沙箱内找到）  
&ensp;|--/api    
&ensp;|&emsp;&emsp;|--alipay.py  #用于计算alipay接口等  
&ensp;|&emsp;&emsp;|--sign.py  #存放一些用于RSA签名和校验RSA签名的方式  
&ensp;|&emsp;&emsp;|--uitls.py  #存放一些小function  
## 已知issues
1. 若用户支付后不等待跳转至/callback，则flask会接收不到项目
