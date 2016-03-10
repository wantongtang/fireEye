#-*-encode utf-8-*-
# 生成签名测试

import hmac
msg = '123999'
key = '123456'
print hmac.new('123456',msg).hexdigest()
