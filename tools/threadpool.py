# thread pool
#
# @auther jason.zhou

import Queue
import threading
import sys
import time
import urllib

class SubThread(threading.Thread):
	def __init__(self, workQueue,timeout=30, **kwargs):
	    threading.Thread.__init__(self, kwargs=kwargs)
	    self.timeout = timeout
	    self.setDaemon(True)
	    self.workQueue = workQueue
	    self.start()
 
 	def run(self):
	    while True:
		    try:
		    	#print('runing.....')
		    	callable,future, args, kwargs = self.workQueue.get(timeout=self.timeout)
		    	future.setThread(self)
		    	res = callable(args, kwargs)
		    	#print 'result....--->'+res
		    	future.setResult(res)
		    except Queue.Empty:
		    	#break
		    	print 'waiting task......'
		    except :
		    	print 'except.....'
		    	print sys.exc_info()
		    	raise

class ThreadPool:
   	def __init__( self, num_of_threads=10 ):
	   self.workQueue = Queue.Queue()
	   self.threads = []
	   self.__createThreadPool( num_of_threads )
 

  	def __createThreadPool( self, num_of_threads ):
  		global thread
  		for i in range( num_of_threads ):
  		    thread = SubThread( self.workQueue)
  		    self.threads.append(thread)
 
    #to delete
  	#def wait_for_complete(self):
  	#	global  thread
  	# 	while len(self.threads):
   	#	 	thread = self.threads.pop()
    #		if thread.isAlive():
    #			print "waiting for "+thread.getName()
    # 			thread.join()
     

  	def add_job( self, callable, *args, **kwargs ):
  		#print 'add job......'
  		future = Future()
  		self.workQueue.put( (callable,future,args,kwargs))
  		return future;



class Future:
	def __init__( self, THREAD=None):
	    self.thread = THREAD
	    self.result = None

	def get(self,timeout=0.2):
		if self.result is None:
			time.sleep(timeout)
			return None
		else:
			return self.result
			
	def setThread(self,thread):
		self.thread=thread

	def setResult(self,result):
		self.result=result
		#print 'self result:'+result
