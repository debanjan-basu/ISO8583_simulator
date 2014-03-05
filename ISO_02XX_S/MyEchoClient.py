"""

(C) Copyright 2009 Igor V. Custodio

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""


from ISO8583.ISO8583 import ISO8583
from ISO8583.ISOErrors import *
import socket
import sys
import time


# Configure the client
serverIP = "10.57.210.23" 
serverPort = 8583
numberEcho = 5
timeBetweenEcho = 5 # in seconds

bigEndian = True
#bigEndian = False

s = None
for res in socket.getaddrinfo(serverIP, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
		s = socket.socket(af, socktype, proto)
    except socket.error, msg:
	s = None
	continue
    try:
		s.connect(sa)
    except socket.error, msg:
	s.close()
	s = None
	continue
    break
if s is None:
    print ('Could not connect :(')
    sys.exit(1)
	
	
	
for req in range(0,numberEcho):
	iso = ISO8583()
	#Modifications for our protocol
	iso.redefineBit(18, '18', 'Merchant Category Code', 'N', 4, 'n')
	iso.redefineBit(60, '60', 'Additional Data', 'LLL', 999, 'ans')
	iso.redefineBit(62, '62', 'Additional Data', 'N', 26, 'ans')

	isoMessage = '0200723C648108E0801C1640320370945546112800000000000010000228121605917114041605022818126051826812800600003140581291711400000001000980020002997PAYPAL Lewinsky Gus      4029357733   LU0360670033000513174261    63428                                   004400716601410405812917114    018114032037094554611                  01812Gus Lewinsky    0201363428 Broad Street                 01014Clovelly                 00416JO 00418AAY000000000000000     00   '

	truncatedIsoMessage = isoMessage[4:1024]
	print truncatedIsoMessage
	#iso.setMTI('0200')
	#iso.setBit(3,'300000')	
	#iso.setBit(24,'045')	
	#iso.setBit(41,'11111111')	
	#iso.setBit(42,'222222222222222')	
	#iso.setBit(63,'This is a Test Message')
	iso.setIsoContent(isoMessage)
	if bigEndian:
		try:
			message = iso.getNetworkISO() 
			s.send(message)
			print ('Sending ... %s' % message)
			ans = s.recv(2048)
			print ("\nInput ASCII |%s|" % ans)
			isoAns = ISO8583()
			isoAns.setNetworkISO(ans)
			v1 = isoAns.getBitsAndValues()
			for v in v1:
				print ('Bit %s of type %s with value = %s' % (v['bit'],v['type'],v['value']))
				
			if isoAns.getMTI() == '0210':
				print ("\tThat's great !!! The server understand my message !!!")
			else:
				print ("The server dosen't understand my message!")
					
		except InvalidIso8583, ii:
			print ii
			break	
		

		time.sleep(timeBetweenEcho)
		
	else:
		try:
			message = iso.getNetworkISO(False) 
			s.send(message)
			print ('Sending ... %s' % message)
			ans = s.recv(2048)
			print ("\nInput ASCII |%s|" % ans)
			isoAns = ISO8583()
			isoAns.setNetworkISO(ans,False)
			v1 = isoAns.getBitsAndValues()
			for v in v1:
				print ('Bit %s of type %s with value = %s' % (v['bit'],v['type'],v['value']))
					
			if isoAns.getMTI() == '0810':
				print ("\tThat's great !!! The server understand my message !!!")
			else:
				print ("The server dosen't understand my message!")
			
		except InvalidIso8583, ii:
			print ii
			break	
		
		time.sleep(timeBetweenEcho)

		
		
print ('Closing...')		
s.close()		
		
