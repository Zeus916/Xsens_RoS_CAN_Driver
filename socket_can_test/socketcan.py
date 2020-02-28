import socket, sys

sock = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
sock.bind(("can0",))

while True:
    can_pkt = sock.recv(16)
    print(can_pkt)
