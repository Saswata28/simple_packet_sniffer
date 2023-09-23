import socket
from scapy.all import *

sniffer_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
try:
    interface = 'eth0'
    sniffer_socket.bind((interface, 0))
except:
    interface = 'wlan0'
    sniffer_socket.bind((interface, 0))


try:
    while True:
        raw_data, addr = sniffer_socket.recvfrom(65535)
        packet = Ether(raw_data)
        print(packet.summary())
except KeyboardInterrupt:
    sniffer_socket.close()
