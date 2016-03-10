# -*-encode utf-8-*-
# send_result.py
import urllib,urllib2
import hmac
from insert_a_task import delete_a_task
from close_task import close_task
import re
import os
import random 
import MySQLdb

def get_and_send_result(qid):
	try:
		conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'wtt@564', port = 3306 )
		cur = conn.cursor()
		conn.select_db('kali')
		
		cmd = 'select * from result_ports where taskid = ' + qid + ';'
		count = cur.execute(cmd)
		print count
		results = cur.fetchall()
		for row in results:
			print row[2]
			send_result(qid,row[3],row[4],row[2],row[5]+' '+ row[8])
		print 'send result done'	
		close_task(qid)
		print 'task closed'
		delete_a_task(qid)
		print 'task finished'
		conn.commit()
		cur.close()
		conn.close()
	except MySQLdb.Error,e:
		print 'MySQL Error %d : %s' %(e.args[0],e.args[1])

	
def send_result(qid,ip,port,last_time,description):
	# signature and communication
	key = '123456'
	msg = str(random.uniform(1,100))
	sign = hmac.new(key,msg).hexdigest()
	#url = 'http://localhost/test999.php'
	url = 'http://wtf.thinkphp.com/index.php?m=index&c=tools&a=getdataport'

	values = {'msg':msg,'sign':sign,'type':1,'qid':qid,'ip':ip,'port':port,'is_open':1,'last_time':last_time,'description':description}

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









