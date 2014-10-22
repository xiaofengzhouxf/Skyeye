#
# mysql client
#
# @auther jason.zhou

import _mysql.MySQLdb as mdb

# mysql client tool
class mysqlcli:

	def __ini__(self):
		self.conn = None
	 
	#connect to db
	#
	#@return if failed ,raise exception, else success
	def connect(self,host="localhost",user="root",passwd="",db="monitor"):
		try:
			self.conn = mdb.connect(host,user,passwd,db)
		except mdb.Error, e:
		    print "Error %d: %s" % (e.args[0],e.args[1])
		    raise e

	#close the connection
	def close(self):
	    if self.conn:    
	        self.conn.close()


    #execute db
    #
    #@return cur:  return the Cursor for this execute
	def exect(self,sql):
		cur = self.conn.cursor()
		cur.execute(sql)
		return cur
		 

	#query db
	#
	#@return rows:  all result rows
	def query(self,sql):
		try:
			cur = self.exect(sql)
			ret = cur.fetchall()
		finally:
			if cur:
				cur.close()
		return ret	

	#insert db
	#
	#@return  if success return true  or failed return false
	def insert(self,sql):
	    try:
	    	cur = self.exect(sql)
	    	self.conn.commit()
	    	return True
	    except:
	    	self.conn.rollback()
	    	print "Insert Error %d: %s" % (e.args[0],e.args[1])
	    	return False
	    finally:
	    	if cur:
	    		cur.close();

	#delete db
	#@return  if success return true  or failed return false
	def delete(self,sql):
		try:
			cur = self.exect(sql)
			self.conn.commit()
			return True
		except mdb.Error, e:
			self.conn.rollback()
			print "Delete Error %d: %s" % (e.args[0],e.args[1])
			return False
		finally:
			if cur:
				cur.close();

	#update db
	#@return  if success return true  or failed return false
	def update(self,sql):
		try:
			cur = self.exect(sql)
			self.conn.commit()
			return True
		except:
			self.conn.rollback()
			print "Upadte Error %d: %s" % (e.args[0],e.args[1])
			return False
		finally:
			if cur:
				cur.close();

##test
if __name__ == '__main__':
	mysqlc = mysqlcli();

	try:
		#connect
		mysqlc.connect();

		print "==========insert============="

		r = mysqlc.insert("INSERT INTO monitor.test(VALUE) VALUES('Jack London')")
		print r

		print "==========select============="
		r = mysqlc.query("SELECT * FROM monitor.test m")
		print r[0]

		print "==========update============="
		r = mysqlc.update("update monitor.test set value='jason' where id = 7")
		print r

		print "==========update============="
		r = mysqlc.delete("delete from monitor.test where id = 10")
		print r

	finally:
		mysqlc.close()

