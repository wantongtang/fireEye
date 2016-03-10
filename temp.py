# -*-encode utf-8-*-
#post.py
import urllib,urllib2
import hmac
from test import insert_a_task
import re
import os
import random 


# signature and communication
key = '123456'
msg = str(random.uniform(1,100))
sign = hmac.new(key,msg).hexdigest()
#url = 'http://localhost/test999.php'
url = 'http://wtf.thinkphp.com/index.php?m=index&c=tools&a=sureport'


values = {'msg':msg,'sign':sign,'qid':25}
data = urllib.urlencode(values)
req =  urllib2.Request(url,data)
res = urllib2.urlopen(req).read()


print res


# task insert into mysql
#insert_a_task(b[0],b[1])
#cmd = 'python ./wyportmap/wyportmap.py ' + b[1] +' ' + b[0]
#os.system(cmd)
# select result from mysql and send to apache






# read a task and run it ,if done return 1 else return 0









