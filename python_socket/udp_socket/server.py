import socket

aim_address = ('127.0.0.1', 31501)
self_address = ('127.0.0.1', 31502)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.settimeout(10)
#s.settimeout(None)
#s.setblocking(0)
s.bind(self_address)

while True:

    data, addr = s.recvfrom(2048)

    if not data:
        print "client has exist"
        break

    print "received:", data, "from", addr
    s.sendto("send ok!", aim_address)

s.close()
