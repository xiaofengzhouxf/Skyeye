# mysql conntion pool
#
# @auther jason.zhou

import db,Queue

class MysqlConnPool:
	"""docstring for MysqlConnPool"""

	global queue;
 

	def __init__(self,timeout=1,size=5,host="localhost",user="root",passwd="",db="monitor"):
		if size <= 0:
			size = 5

		queue = Queue.Queue(maxsize = 5)

		for i in range(size):
			queue.put(newDB(host,user,passwd,db))


	def newDB(self,host="localhost",user="root",passwd="",db="monitor"):
		return db(host,user,passwd,db)



	#borrow db from pool
	#Should return db after finish the method.
	#
	# try:
	#    db_ = db.borrowDB()
	#    xxxxx
	# finally:
	#    db_.returnBD()
	def borrowDB(self):
		return queue.get(timeout)



	#return db to pool
	def returnDB(self,db):
		queue.put(db)




