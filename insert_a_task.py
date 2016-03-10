from mysql import *

def insert_a_task(id,state):
	str = 'insert into task_running  values(' + id + ',' + '\''+state + '\''+ ' );'
	return do_mysql_operate(str)
	#print str

def delete_a_task(id):
	str = 'delete from task_running where taskid = ' + id + ';'
	return do_mysql_operate(str)

	
