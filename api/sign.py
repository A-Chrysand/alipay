import OpenSSL
from base64 import b64encode, b64decode


def rsa2_sign(message, key):
	"""
	rsa2签名
	:param message: 待签名数据(bytes)
	:param key: 私钥(bytes)
	:return: 数据签名信息(bytes)
	"""

	private_key = OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, key)
	m = OpenSSL.crypto.sign(private_key, message, 'sha256')
	return b64encode(m)


def signCheck(message, sign, key):
	"""
	rsa2签名验证
	:param message: 进行签名的数据(bytes)
	:param sign: 数据的签名信息(bytes)
	:param key: 公钥(bytes)
	:return:
	"""

	if not isinstance(message, bytes):
		message = message.encode()
	if not isinstance(sign, bytes):
		sign = sign.encode()
	if not isinstance(key, bytes):
		key = key.encode()
	b64_key = b64decode(key)
	try:
		public_key = OpenSSL.crypto.load_publickey(OpenSSL.crypto.FILETYPE_ASN1, b64_key)
		X = OpenSSL.crypto.X509()
		X.set_pubkey(public_key)
		OpenSSL.crypto.verify(X, b64decode(sign), message, 'sha256')
		return True
	except:
		return False
