# -*-encode utf-8-*-
#post.py
# confirm that I have receved task,and send to server 
import urllib,urllib2
import hmac
from test import insert_a_task
import re
import os
import random 

def confirm(qid):
# signature and communication
	key = '123456'
	msg = str(random.uniform(1,100))
	sign = hmac.new(key,msg).hexdigest()
	#url = 'http://localhost/test999.php'
	url = 'http://wtf.thinkphp.com/index.php?m=index&c=tools&a=sureport'

	values = {'msg':msg,'sign':sign,'qid':qid}
	data = urllib.urlencode(values)
	req =  urllib2.Request(url,data)
	res = urllib2.urlopen(req).read()
	return res

















