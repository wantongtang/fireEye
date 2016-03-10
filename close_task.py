# -*-encode utf-8-*-
# close_task.py
import urllib,urllib2
import hmac
from insert_a_task import insert_a_task
import re
import os
import random 

def close_task(qid):

# signature and communication
	key = '123456'
	msg = str(random.uniform(1,100))
	sign = hmac.new(key,msg).hexdigest()
#url = 'http://localhost/test999.php'
	url = 'http://wtf.thinkphp.com/index.php?m=index&c=tools&a=completeport'
	values = {'msg':msg,'sign':sign,'qid':qid}	
	data = urllib.urlencode(values)
	req =  urllib2.Request(url,data)
	res = urllib2.urlopen(req).read()
	b = re.findall('\n\n(.*?)\n\n',res)
	print res
	print b
# task insert into mysql
#insert_a_task(b[0],b[1])
#if res == 'none':
#	print 'passed'
#else if res == 'bad request!':
#else:
#	cmd = 'python ./wyportmap/wyportmap.py ' + b[1] +' ' + b[0]
#	os.system(cmd)
# select result from mysql and send to apache






# read a task and run it ,if done return 1 else return 0









