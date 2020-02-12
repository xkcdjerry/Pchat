# bootstrap.py
import tutils
import socket
def ping(ip,port):
    try:
        sock = tutils.csock(ip,port)
    except tutils.ConnectionError:
        return
    sock.send(tutils.CLIENT_PING)
    try:
        ans = sock.recv(1)
        if ans==tutils.SERVER_ACK:
            return sock
        else:
            return
    except tutils.ConnectionTimeOut:
        return
        
    
def strap() -> tutils.Client:
    for ip,port in tutils.defaults:
        sock=ping(ip,port)
        if sock:
            return tutils.Client(sock)
