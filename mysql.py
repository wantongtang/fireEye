# mysql.py
# connect mysql database

import MySQLdb

def do_mysql_operate(str):
	try:
		conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd  = 'wtt@564',db = 'task',port =  3306)
		cur = conn.cursor()

		count = cur.execute(str)
		conn.commit()
		cur.close()
		conn.close()
		return count
	except MySQLdb.Error,e:
		print "mysql error %d:%s" %(e.args[0],e.args[1])
		return 0
