print (' Bienvene Dans SQAN2PORT')
import socket
import sys

Ip = raw_input('ip a scanner: ')
print(' Scan de l\'ip : ' + Ip + ' en cours...' )
try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((Ip, port))
        if result == 0:
            print(' Port ' + str(port) + ' Ouvert')
            sock.close()
except socket.gaierror:
    print(' serveur non joignable ')
    sys.exit()
except socket.error:
    print(' serveur non joignable ')
    sys.exit()

print(' Scan finis ')
