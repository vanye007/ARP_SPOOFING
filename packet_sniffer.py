import scapy.all as scapy
#from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffed_packets, filter="port 80")

def sniffed_packets(packet):
    print(packet.show())
    #if packet.haslayer(http.HTTPRequest):
        #print(packet.show())
        #url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        #print(url)

sniff("eth0")
