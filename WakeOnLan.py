""""
Send Magic Package for Wake on Lan
""""

import socket
import struct

# insert correct MAC address
MAC = 'FF:FF:FF:FF:FF:FF'

MAC = MAC.replace(':','')
    
magic_packet = ''.join(['FF' * 6, MAC * 16])

send_data = b''
for i in range(0, len(magic_packet), 2):
    send_data = b''.join([send_data, struct.pack('B', int(magic_packet[i: i + 2], 16))])

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
soc.sendto(send_data, ("255.255.255.255", 9))


