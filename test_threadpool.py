from threadpool import *

def test_job(id, sleep = 0.001 ):
	global html
	try:
		html="test--->"+str(id)
		print html
	except:
		print  sys.exc_info()
	finally:
		return  html
 
def test():
	futures=[]
	delFuture=[]
	
	print 'start testing'
	tp = ThreadPool(10)
	for i in range(10):
		#print 'start.......'
		time.sleep(0.2)
		futures.append(tp.add_job( test_job, i, i*0.001 ))


	while len(futures):
		print 'futures len:'+str(len(futures))
		
		if (len(futures)==len(delFuture)):
			break;

		for i in range(len(futures)):
			if(i in delFuture):
				print str(i)+'is in del futures'
				continue

			print 'loop: '+str(i)
			res = futures[i].get()
			if res is None:
				time.sleep(0.5)
				print 'wait....'
			else:
				print str(i)+' result: '+res
				delFuture.append(i)
				


	print 'end testing'
 
if __name__ == '__main__':
	test()