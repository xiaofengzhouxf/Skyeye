# Socket server
# @auther jason.zhou

import socket
import sys

class monitorServer:
	running = False

	def __init__(self,HOST=None,PORT=50007):
		self.host=HOST
		self.port=PORT

	def startServer(self):
		s = None
		for res in socket.getaddrinfo(self.host, self.port, socket.AF_UNSPEC,
		                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
		    af, socktype, proto, canonname, sa = res
		    try:
		        s = socket.socket(af, socktype, proto)
		    except socket.error as msg:
		        s = None
		        continue
		    try:
		    	#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) ## reused TIME_WAIT state connect
		        s.bind(sa)
		        s.listen(1)
		        running = True;
		    except socket.error as msg:
		        s.close()
		        s = None
		        continue
		    break
		if s is None:
		    print 'could not open socket'
		    #sys.exit(1)

		try:
			while running:    
				conn, addr = s.accept()
				print 'Connected by', addr
				proc = monitorProcess()
				proc.process(conn,addr)
	
		finally:
			s.close();

	def closeServer(self):
		running=False

	##start a thread to deal a conn
class monitorProcess:
	def porcess(self,conn,addr):
   		data = conn.recv(1024)
		if not data: 
			raise
		conn.send('server:'+addr+'-->'+data)

class MonitorExcept(Exception):
	"""docstring for MonitorException"""

	def __init__(self, arg):
		super(MonitorException, self).__init__()
		self.arg = arg


		


if __name__ == '__main__':
	server = monitorServer()
	server.startServer()
	sys.exit(1)