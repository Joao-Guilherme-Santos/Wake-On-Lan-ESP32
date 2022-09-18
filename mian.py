import network
from time import sleep
import socket

ssid = 'your ssid'
password = 'your password'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,password)
while wlan.isconnected() != True:
    print('.', end='')
    sleep(1)
    pass
print()
print('CONECTADO')


BROADCAST_IP = "255.255.255.255"
DEFAULT_PORT = 9

def send_magic_packet(
    ip_address: str = BROADCAST_IP,
    port: int = DEFAULT_PORT,
    interface: str = None
) -> None:

    packets = [b'\xff\xff\xff\xff\xff\xff\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a\x14\xda\xe9\xf2\xa2\x1a']

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if interface is not None:
        sock.bind((interface, 0))
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.connect((ip_address, port))
    for packet in packets:
        sock.send(packet)
        
        
send_magic_packet()
