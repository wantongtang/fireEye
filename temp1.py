#from confirm import confirm
from request_task import request_task
#from send_result import send_result
#print confirm(26)

from mysql import do_mysql_operate



cmd = 'select * from task_running;'
count = do_mysql_operate(cmd)

if count < 2: # finate  the number of tasks
	request_task()# request a task and put it in mysql,then send a confirm information to php-let
else:
	print 'the number of task is out of %s' % count














