import socket

aim_address = ('127.0.0.1', 31502)
self_address = ('127.0.0.1', 31501)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.settimeout(0.1)
s.bind(self_address)
while True:
    msg = raw_input()
    if not msg:
        break
    s.sendto(msg, aim_address)
    try:
        data, addr = s.recvfrom(2048)
    except socket.timeout:
        print "client"
        continue
    if not data:
        print "client has exist"
        break
    print "received:", data, "from", addr

s.close()