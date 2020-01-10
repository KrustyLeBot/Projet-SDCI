import http.server
import socketserver
from threading import Thread
from time import sleep

#1 => pas encore configuree, 2 => loadbalancer, 3 => leakybucket
vnf_type = 1

srv = ""
srv1 = ""
srv2 = ""

index = 0;
vnf_buffer = []


#thread for leakybucket
class MonThread (Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		print("Thread running")
		global vnf_buffer
		while(1):
			if(len(vnf_buffer)>0):
				tmp = vnf_buffer[0]
				print("on vide")
				print(tmp.path)
				tmp.send_response(301)
				tmp.send_header('Location',srv)
				tmp.end_headers()
				del vnf_buffer[0]
			sleep(2)


class myHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		global vnf_type
		global srv1
		global srv2
		global index
		global vnf_buffer

		print(self.path) 

		path_list = self.path.split("/")

		if("configure_type" in self.path):
			vnf_type = path_list[len(path_list)-1]
			print(vnf_type)

			if(vnf_type == '3'):
				#start thread that empty the bucket on a clock shift
				thread1 = MonThread()
				thread1.start()

			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write("Done".encode('utf-8'))

		elif("configure_srv" in self.path):
			srv = path_list[len(path_list)-2] + ":" + path_list[len(path_list)-1]
			print(srv)
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write("Done".encode('utf-8'))

		elif("configure_srv1" in self.path):
			srv1 = path_list[len(path_list)-2] + ":" + path_list[len(path_list)-1]
			print(srv1)
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write("Done".encode('utf-8'))

		elif("configure_srv2" in self.path):
			srv2 = path_list[len(path_list)-2] + ":" + path_list[len(path_list)-1]
			print(srv2)
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write("Done".encode('utf-8'))

		elif("ping" in self.path):
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write("Pong".encode('utf-8'))


		#Loadbalancer
		######################################################################
		elif(vnf_type == '2'):
			print(index)

			if(index == '0'):
				print("redirect to " + srv1 + self.path)
				self.send_response(301)
				self.send_header('Location',srv1)
				self.end_headers()
			else:
				print("redirect to " + srv2 + self.path)
				self.send_response(301)
				self.send_header('Location',srv1)
				self.end_headers()
			index = index + 1
		######################################################################


		#Loeakybucket
		######################################################################
		elif(vnf_type == '3'):
			print("Ajout " + self.path)
			vnf_buffer.append(self)
		######################################################################

		

theport = 8080
Handler = myHandler
pywebserver = socketserver.TCPServer(("", theport), Handler)

print("Python based web server. Serving at port", theport)
pywebserver.serve_forever()