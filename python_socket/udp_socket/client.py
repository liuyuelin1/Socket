import socket

address = ('127.0.0.1', 31501)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.settimeout(10)
while True:
    msg = raw_input()
    if not msg:
        break
    s.sendto(msg, address)

s.close()