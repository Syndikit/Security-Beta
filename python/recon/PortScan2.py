import socket, threading

host = input("Enter address to scan: ")

ip = socket.gethostbyname(host)
threads = []
open_ports = {}

def poke_port(ip, port, delay, open_ports):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.settimeout(delay)
    result = s.connect_ex((ip, port))

    if result == 0:
        open_ports[port] = 'open'
        return True
    else:
        open_ports[port] = 'false'
        return None

def scan_port(ip, delay):

    for port in range(0,1023):
        thread = threading.Thread(target = poke_port, args = (ip, port, delay, open_ports))
        threads.append(thread)

    for i in range(0, 1023):
        threads[i].start()

    for i in range(0, 1023):
        threads[i].join()
    
    for i in range(0, 1023):
        if open_ports[i] == 'open':
            print('\nport number: '+str(i)+' is open.')
        if i == 1022:
            print('Scan complete.')

if __name__ == '__main__':
    scan_port(ip, 3)