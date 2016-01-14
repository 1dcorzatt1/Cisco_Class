#!/usr/bin/env python
import sys 

if __name__ == "__main__":
    print 'It is about time I started programming.'


#!/usr/bin/env python
def getRouter (rtr) :
	router1 = {'os_version':'3.1.1','hostname':'nyc_router1','model':'nexus 9396','domain':'cisco.com','mgmt_ip':'10.1.50.11'}

	router2 = dict( os_version='3.2.1', hostname='rtp_router2',model='nexus 9396', domain='cisco.com', mgmt_ip='10.1.50.12')

	router3 = dict( os_version='3.1.1', hostname='ROUTER3',model='nexus 9504', domain='lab.cisco.com', mgmt_ip='10.1.50.13')

	router_list = [router1,router2,router3]
	for router in router_list:
		if rtr == router['hostname']:
			return router

	return 'No router found.'


if __name__ == "__main__":

	args = sys.argv

	print "ARGUMENTS: ",args
	print "First argument: ", args[0]

	print "Second argument: ",args[1]


	result1 = getRouter('nyc_router1')
	print result1

	print 'HOSTNAME:', result1['hostname']
	print 'Model:', result1['model']

	result2 = getRouter('Router3')
	print result2



	







