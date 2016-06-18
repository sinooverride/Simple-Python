#!/usr/bin/env python

import urllib.request as urlrequest
import re


def ip_v4():
	request = urlrequest.urlopen("http://checkip.dyndns.org/").read()
	output = request.decode('utf-8')

	IPv4 = re.findall("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", output)
	value = IPv4[0]
	print ("IP V4: ", value)
	print ("")

def ip_v6():
	request = urlrequest.urlopen("http://show-my-ip.de").read()
	output = request.decode('utf-8')
	
	IPv6 = re.findall("IP is (.+?)</title>", output)
	value = IPv6[0]
	x = (":")
	if x in value:
		print("IP V6:", value)
		print("")
	else:
		print("IPv6:   (only IPv4)")
		print("")


if __name__ == "__main__":
	print ("Getting externel IP")
	print ("-"*19)
	ip_v4()
	ip_v6()
