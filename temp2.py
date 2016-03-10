#!/usr/lib/env python
import MySQLdb

try:
	conn = MySQLdb.connect(host = 'localhost',user = 'root',passwd = 'wtt@564',port = 3306)
	cur = conn.cursor()

	conn.select_db('kali')

	count = cur.execute('select * from result_ports')
	print 'there has %s rows record' % count

	result = cur.fetchone()
	print result
	print 'ID:%s infor %s' % result

	results = cur.fetchmany(5)
	for r in results:
		print r
	print '==' * 10
	cur.scroll(0,mode='absolute')



	conn.commit()
	cur.close()
	conn.close()


except MySQLdb.Error,e:
	print 'MySQL Error %d: %s' %(e.args[0],e.args[1])



