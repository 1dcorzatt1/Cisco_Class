#/usr/bin/env python

import xmltodict 
import json
from device import Device 

def show_intf_mgmt(sw):

	getdata = sw.show('show interface mgmt0')

	show_intf_dict = xlmtodict.parse(getdata[1])

	data = show_intf__dict['ins_api']['outputs']['output']['body']'TABLE_Interface']['ROW_interface']

	ip = data['eth_ip-addr']
	mask = data['eth_ip_mask']
	name = data['interface']
	speed = data['eth_speed']
	duplex = data['eth_duplex']

	mgmt_dict = { 'ip_addr': ip+'/'+mask, 'name':name, 'speed': speed, 'duplex': duplex }

	print json.dumps(mgmt_dict, indent=4)

	return mgmt_dict

	


