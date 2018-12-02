#!/usr/bin/python

from scapy.all import *
import pprint

pkt = rdpcap('deauth.pcap')
deauthPacket = pkt[6130]
pprint.pprint(dir(deauthPacket))

deauthPacket.show()
deauthPacket.pdfdump('pkt.pdf')


print(deauthPacket.summary())

hexdump(deauthPacket)

pprint.pprint(RadioTap(deauthPacket))
