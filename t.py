from scapy.all import *

for i in range(254)
  requested_addr = f'10.1.10.{i}'
  response = dhcp_request(req_type='request', requested_addr=requested_addr)
  
  if response and DHCP in response:
      print("DHCP ACK received:", response[DHCP])
