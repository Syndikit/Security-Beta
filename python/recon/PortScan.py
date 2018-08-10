#Purpose: Create a multi-threaded port scanner
# Imports vanilla socket module: low level networking interface 
import socket, threading
# nmap is a tool to automatize scanning task and reports.
#import nmap


host = input("Enter address to scan: ")

"""
Creates a host name from ip address entered
threads is a list that will store our multi threaded
""" 
ip = socket.gethostbyname(host)
threads = []
open_ports = {}

"""
Method for testing whether port is open or not and stores ports classified as 'open' or 'closed' in open_ports dictionary (map)
"""
def poke_port(ip, port, delay, open_ports):
    """ 
    Creates a new socket and takes in the default address and protocol families 
    (AF_INET) and socket types (SOCK_STREAM)
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Uses default socket options and sets a delay of 1 second
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.settimeout(delay)
    result = s.connect_ex((ip, port))

    # If a connection exists, result will return True (0) and that port number in the open_ports dictionary will be mapped to string 'open' 
    if result == 0:
        open_ports[port] = 'open'
        return True
    else:
        open_ports[port] = 'false'
        return None

"""
Method for scanning ports at the ip address user inputs, with a specified delay.

"""
def scan_port(ip, delay):
    
    # Creates new threads that 'poke' or test ports for openness
    for port in range(0,1023):
        thread = threading.Thread(target = poke_port, args = (ip, port, delay, open_ports))
        threads.append(thread)
    
    # Starts a new thread for each port in range given below.
    for i in range(0, 1023):
        threads[i].start()

    # Allows master thread to call more threads that scan ports before the earlier ones finish (Yay multi-threading!) 
    for i in range(0, 1023):
        threads[i].join()
    
    # Creates a concise, formatted output of iterating through the open_ports list in the terminal of only the ports that are actually 'open'. 
    for i in range(0, 1023):
        if open_ports[i] == 'open':
            print('\nport number: '+str(i)+' is open.')
        if i == 1022:
            print('Scan complete.')

# Calls methods defined above. 
if __name__ == '__main__':
    # Sets default timeout to 3 seconds
    scan_port(ip, 3)