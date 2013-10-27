## Harvester.py
import sys
import HarvesterServer
import HarvesterClient
import socket

mode = ""

def serverMode():
	myServer = HarvesterServer.HarvesterServer()
	
	
def clientMode(ip):
	myClient = HarvesterClient.HarvesterClient(ip)
	#Assuming client is at this point ready to go
	#wait for user to input a command, then queue up that command

def main():
	if len(sys.argv) < 2:
		print "Usage: Harvester <Server|Client> (Client address)"
		print "e.g.: Python Harvester.py Server"
		print "or: Python Harvester.py Client 10.0.10.1"
		sys.exit()	
			
	global mode
	mode = sys.argv[1]
	if mode == "server":
		serverMode()
		
	elif mode == "client":
		if len(sys.argv) == 3:
			print "Connecting to your own server"
			ip = sys.argv[2]
		if len(sys.argv) == 2:
			print "Defaulting to using developer's cluster"
			ip = socket.gethostbyname('play4trickster.cloudapp.net')
		clientMode(ip)	


if __name__ == '__main__':
	main()
