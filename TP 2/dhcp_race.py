from scapy.all import DHCP_am, Net

dhcp_server = DHCP_am(
    iface='enp0s3',
    domain='yolo.internal',
    pool=Net('10.1.10.55/24'),
    network='10.1.10.0/24',
    gw='10.1.10.254',
    nameserver=['9.9.9.9'],
    renewal_time=600,
    lease_time=3600
)

dhcp_server()
