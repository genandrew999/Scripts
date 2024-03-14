#!/bin/python3

import sys
import socket
from datetime import datetime

def validate_IP(address):

	parts = address.split(".")
	octect = map(int, parts)

	if len(parts) != 4:
	
		return False

	for part in octect:
	
		if not isinstance(part, int):
		
			return False

		if part < 0 or part > 255:
		
			return False

	return True

target = sys.argv[1]
	
if validate_IP(target) == True:
	
	print("-" * 50)
	print("Target: "+target)
	print("Time Started: "+str(datetime.now()))
	print("-" * 50) 

	try:
		
		for port in range(0,65535):
			
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target,port))

			if result == 0:
					
				print(f"Port {port} is open.")

			s.close()

	except KeyboardInterrupt:
			
		print("\nExiting Program")
			
		sys.exit()

	except socket.gaierror:
			
		print("\nHostname could not be resolved.")
			
		sys.exit()

	except socket.error:
	
		print("\nCould not connect to server.")
		sys.exit()

else:

	print("Error! Please use the following syntax with a valid IP address.\n")
	print("Syntax: python3 scanner.py <192.168.1.1>")
