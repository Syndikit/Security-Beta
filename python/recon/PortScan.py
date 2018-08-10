# Imports vanilla socket module: low level networking interface 
import socket
# nmap is a tool to automatize scanning task and reports.
#import nmap

# Sets default timeout to 2 seconds
socket.setdefaulttimeout(2)

""" 
Creates a new socket and takes in the address and protocol families 
(AF_INET) and socket types (SOCK_STREAM)
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = 'pythonprogramming.net/'

# Prompts user for web URL text input
#target = input('What website to scan?: ')

#s.connect(('192.168.1.112', 12730))

def portscan(port):
    try:
        s.connect(target, port)
        return True
    except:
        return False

for x in range(10000, 10103):
    if(portscan(x)):
        print('Port ', x, 'is open.')
    else:
        print('Port: ', x, ' is closed.')

# Answer from pinging local system and prints next 1024 bytes to terminal
#answer = s.recv(1024)

#print(answer)

#nm = nmap.PortScanner()