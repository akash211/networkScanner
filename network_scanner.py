#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\t\tMAC Address\n------------------------------------------")
    for element in answered:
        print(element[1].psrc, "\t\t\t", element[1].hwsrc)
        print("------------------------")


scan("192.168.136.1/24")
