"""

(C) Copyright 2009 Debanjan Basu(debanjan.basu@gmail.com)

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

import socket, subprocess, re
#Utility subroutines
def get_ipv4_address():
    """
    Returns IP address(es) of current machine.
    :return:
    """
    p = subprocess.Popen(["/sbin/ifconfig"], stdout=subprocess.PIPE)
    ifc_resp = p.communicate()
    patt = re.compile(r'inet\s*\w*\S*:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    resp = patt.findall(ifc_resp[0])
    #print resp
    return resp[0]
    

#Validation sub routines
def validate_BM_1(bitype, bitvalue):	
	 print "The bitype is ", str(bitype), "The bitvalue : " , str(bitvalue)
	 raise InvalidIso8583, "Invalid Bitmap" 
	 return 
#PAN
def validate_BM_2(bitype, bitvalue):
	print "The bitype is ", str(bitype), "The bitvalue : " , str(bitvalue)
	if (bitype != 2):
		raise InvalidIso8583, "Invalid Bitmap_2"
	#check length 
	if (len(str(bitvalue)) != 19):
		raise InvalidIso8583, "Invalid Bitmap_2"
		 
	# should be numeric
	for c in str(bitvalue):
		if (c.isdigit() == False):
			raise InvalidIso8583, "Invalid Bitmap_2"
	return 

#Processing code
def validate_BM_3(bitype, bitvalue):
	#hardcoded processing code
	if (str(bitvalue) != "280000"):
		raise InvalidIso8583, "Invalid Bitmap_3"
	return

#Transaction Amount
def validate_BM_4(bitype, bitvalue):
	
	#check length 
	if (len(str(bitvalue)) != 12):
		raise InvalidIso8583, "Invalid Bitmap_4"

	# should be numeric
	for c in str(bitvalue):
		if (c.isdigit() == False):
			raise InvalidIso8583, "Invalid Bitmap_4"
	return 

#We do not have to check these bitmap
def validate_BM_5(bitype, bitvalue):
	return
def validate_BM_6(bitype, bitvalue):
	return

#Transmission date and time
def validate_BM_7(bitype, bitvalue):
	#check length 
	if (len(str(bitvalue)) != 10):
		raise InvalidIso8583, "Invalid Bitmap_7"
	# should be numeric
	for c in str(bitvalue):
		if (c.isdigit() == False):
			raise InvalidIso8583, "Invalid Bitmap_7"
	return

#oh wow we do not have to check these bitmap
def validate_BM_8(bitype, bitvalue):
	return
def validate_BM_9(bitype, bitvalue):
	return
def validate_BM_10(bitype, bitvalue):
	return

#System Trace number
def validate_BM_11(bitype, bitvalue):
	#check length 
	if (len(str(bitvalue)) != 6):
		raise InvalidIso8583, "Invalid Bitmap_11"

	# should be numeric
	for c in str(bitvalue):
		if (c.isdigit() == False):
			raise InvalidIso8583, "Invalid Bitmap_11"
	return

#Local Transaction time 
def validate_BM_12(bitype, bitvalue):
	#check length 
	if (len(str(bitvalue)) != 6):
		raise InvalidIso8583, "Invalid Bitmap_12"

	# should be numeric
	for c in str(bitvalue):
		if (c.isdigit() == False):
			raise InvalidIso8583, "Invalid Bitmap_12"
	return

#Local Transaction Date
def validate_BM_13(bitype, bitvalue):
	#check length 
	if (len(str(bitvalue)) != 4):
		raise InvalidIso8583, "Invalid Bitmap_13"

	# should be numeric
	for c in str(bitvalue):
		if (c.isdigit() == False):
			raise InvalidIso8583, "Invalid Bitmap_13"
	return

#Card Expiry Date
def validate_BM_14(bitype, bitvalue):
	#check length 
	if (len(str(bitvalue)) != 4):
		raise InvalidIso8583, "Invalid Bitmap_14"

	# should be numeric
	for c in str(bitvalue):
		if (c.isdigit() == False):
			raise InvalidIso8583, "Invalid Bitmap_14"
	return

def validate_BM_15(bitype, bitvalue):
	return

def validate_BM_16(bitype, bitvalue):
	return

def validate_BM_17(bitype, bitvalue):
	return

#Merchant category code
def validate_BM_18(bitype, bitvalue):
	#check length
        if (len(str(bitvalue)) != 4):
                raise InvalidIso8583, "Invalid Bitmap_18"

        # should be numeric
        for c in str(bitvalue):
                if (c.isdigit() == False):
                        raise InvalidIso8583, "Invalid Bitmap_18"
	return

#Country Code
def validate_BM_19(bitype, bitvalue):
	 #check length
        if (len(str(bitvalue)) != 3):
                raise InvalidIso8583, "Invalid Bitmap_19"

        # should be numeric
        for c in str(bitvalue):
                if (c.isdigit() == False):
                        raise InvalidIso8583, "Invalid Bitmap_19"
	return

def validate_BM_20(bitype, bitvalue):
	return
def validate_BM_21(bitype, bitvalue):
	return

#Point of Service Entry Mode
def validate_BM_22(bitype, bitvalue):
	#check length
        if (len(str(bitvalue)) != 3):
                raise InvalidIso8583, "Invalid Bitmap_22"

        # should be numeric
        for c in str(bitvalue):
                if (c.isdigit() == False):
                        raise InvalidIso8583, "Invalid Bitmap_22"
	return

def validate_BM_23(bitype, bitvalue):
	return
def validate_BM_24(bitype, bitvalue):
	return

#POS Condition code
def validate_BM_25(bitype, bitvalue):
	#check length
        if (len(str(bitvalue)) != 2):
                raise InvalidIso8583, "Invalid Bitmap_25"

        # should be numeric
        for c in str(bitvalue):
                if (c.isdigit() == False):
                        raise InvalidIso8583, "Invalid Bitmap_25"
	return

def validate_BM_26(bitype, bitvalue):
	return
def validate_BM_27(bitype, bitvalue):
	return
def validate_BM_28(bitype, bitvalue):
	return
def validate_BM_29(bitype, bitvalue):
	return
def validate_BM_30(bitype, bitvalue):
	return
def validate_BM_31(bitype, bitvalue):
	return

#Bin number, Acquiring institution id code
def validate_BM_32(bitype, bitvalue):
	#check length
        if (len(str(bitvalue)) > 0 and len(str(bitvalue)) <= 10):
                raise InvalidIso8583, "Invalid Bitmap_32"

        # should be numeric
        for c in str(bitvalue):
                if (c.isdigit() == False):
                        raise InvalidIso8583, "Invalid Bitmap_32"
        return

def validate_BM_33(bitype, bitvalue):
	return
def validate_BM_34(bitype, bitvalue):
	return
def validate_BM_35(bitype, bitvalue):
	return
def validate_BM_36(bitype, bitvalue):
	return

#Retreival reference number
def validate_BM_37(bitype, bitvalue):
	if (len(str(bitvalue)) != 12):
		raise InvalidIso8583, "Invalid Bitmap_37"
	# should be alpha-numeric
        for c in str(bitvalue):
                if (c.isalpha() == False):
                        raise InvalidIso8583, "Invalid Bitmap_32"
	return

def validate_BM_38(bitype, bitvalue):
	return
def validate_BM_39(bitype, bitvalue):
	return
def validate_BM_40(bitype, bitvalue):
	return

def validate_BM_41(bitype, bitvalue):
	if (str(bitvalue) != "00000001"):
		raise InvalidIso8583, "Invalid Bitmap_41"
	return

#Merchant Number
def validate_BM_42(bitype, bitvalue):
	#check length
        if (len(str(bitvalue)) != 15):
                raise InvalidIso8583, "Invalid Bitmap_42"

        # should be numeric
        for c in str(bitvalue):
                if (c.isdigit() == False):
                        raise InvalidIso8583, "Invalid Bitmap_42"
	return

#Card Acceptor Name and Location
def validate_BM_43(bitype, bitvalue):

	if (len(str(bitvalue)) != 40):
                raise InvalidIso8583, "Invalid Bitmap_43"
        # should be alpha-numeric
        for c in str(bitvalue):
                if (c.isalpha() == False):
                        raise InvalidIso8583, "Invalid Bitmap_43"
        return

def validate_BM_44(bitype, bitvalue):
		return
def validate_BM_45(bitype, bitvalue):
	return
def validate_BM_46(bitype, bitvalue):
	return
def validate_BM_47(bitype, bitvalue):
	return

def validate_BM_48(bitype, bitvalue):
	#check length
        if (len(str(bitvalue)) > 0 and len(str(bitvalue)) <= 999):
                raise InvalidIso8583, "Invalid Bitmap_48"

        # should be numeric
        for c in str(bitvalue):
                if (c.isalpha() == False):
                        raise InvalidIso8583, "Invalid Bitmap_48"
	return

def validate_BM_49(bitype, bitvalue):

	if (len(str(bitvalue)) != 3):
                raise InvalidIso8583, "Invalid Bitmap_43"
        # should be alpha-numeric
        for c in str(bitvalue):
                if (c.isalpha() == False):
                        raise InvalidIso8583, "Invalid Bitmap_43"
	return
def validate_BM_50(bitype, bitvalue):
	return
def validate_BM_51(bitype, bitvalue):
	return
def validate_BM_52(bitype, bitvalue):
	return
def validate_BM_53(bitype, bitvalue):
	return
def validate_BM_54(bitype, bitvalue):
	return
def validate_BM_55(bitype, bitvalue):
	return
def validate_BM_56(bitype, bitvalue):
	return
def validate_BM_57(bitype, bitvalue):
	return
def validate_BM_58(bitype, bitvalue):
	return
def validate_BM_59(bitype, bitvalue):
	return

#additional data
def validate_BM_60(bitype, bitvalue):
	return
def validate_BM_61(bitype, bitvalue):
	return
def validate_BM_62(bitype, bitvalue):
	return
def validate_BM_63(bitype, bitvalue):
	return
def validate_BM_64(bitype, bitvalue):
	return
def validate_BM_65(bitype, bitvalue):
	return
def validate_BM_66(bitype, bitvalue):
	return
def validate_BM_67(bitype, bitvalue):
	return
def validate_BM_68(bitype, bitvalue):
	return
def validate_BM_69(bitype, bitvalue):
	return

def validate_ISO8583 (bitmap, bitype, bitvalue):
	print "The bitmap is ", str(bitmap)
	print "The bit-type is ", str(bitype)
	print "The bitvalue is ", str(bitvalue)

	try:
		if (str(bitmap) == 2): 
			validate_BM_2(bitmap, bitvalue)
			return
		elif (str(bitmap) == 3): 
			validate_BM_3(bitmap, bitvalue)
			return
		elif (str(bitmap) == 4): 
			validate_BM_4(bitmap, bitvalue)
			return
		elif (str(bitmap) == 7): 
			validate_BM_7(bitmap, bitvalue)
			return
		elif (str(bitmap) == 11): 
			validate_BM_11(bitmap, bitvalue)
			return
		elif (str(bitmap) == 12): 
			validate_BM_12(bitmap, bitvalue)
			return
		elif (str(bitmap) == 13): 
			validate_BM_13(bitmap, bitvalue)
			return
		elif (str(bitmap) == 14): 
			validate_BM_14(bitmap, bitvalue)
			return
		elif (str(bitmap) == 18): 
			validate_BM_18(bitmap, bitvalue)
			return
		elif (str(bitmap) == 19): 
			validate_BM_19(bitmap, bitvalue)
			return
		elif (str(bitmap) == 22): 
			validate_BM_22(bitmap, bitvalue)
			return
		elif (str(bitmap) == 25): 
			validate_BM_25(bitmap, bitvalue)
			return
		elif (str(bitmap) == 32): 
			validate_BM_32(bitmap, bitvalue)
			return
		elif (str(bitmap) == 37): 
			validate_BM_37(bitmap, bitvalue)
			return
		elif (str(bitmap) == 41): 
			validate_BM_41(bitmap, bitvalue)
			return
		elif (str(bitmap) == 42): 
			validate_BM_42(bitmap, bitvalue)
			return
		elif (str(bitmap) == 43): 
			validate_BM_43(bitmap, bitvalue)
			return
		elif (str(bitmap) == 48): 
			validate_BM_43(bitmap, bitvalue)
			return
		elif (str(bitmap) == 49): 
			validate_BM_43(bitmap, bitvalue)
			return
		elif (str(bitmap) == 60): 
			validate_BM_43(bitmap, bitvalue)
			return
		elif (str(bitmap) == 61): 
			validate_BM_43(bitmap, bitvalue)
			return
		elif (str(bitmap) == 62): 
			validate_BM_43(bitmap, bitvalue)
			return
	except	InvalidIso8583, exceptionInfo:
        	print exceptionInfo 
	return

from ISO8583.ISO8583 import ISO8583
from ISO8583.ISOErrors import *
from socket import *

# Configure the server
#serverIP = "10.57.210.23" 
serverIP = get_ipv4_address() 
serverPort = 8583
maxConn = 5
bigEndian = True
#bigEndian = False


# Create a TCP socket
s = socket(AF_INET, SOCK_STREAM)    
# bind it to the server port
s.bind((serverIP, serverPort))   
# Configure it to accept up to N simultaneous Clients waiting...
s.listen(maxConn)                        


# Run forever
while 1:
	#wait new Client Connection
	connection, address = s.accept() 
	while 1:
		# receive message
		isoStr = connection.recv(2048) 
		#isoStr = isoStr[4:2048]
		if isoStr:
			print ("\nInput ASCII |%s|" % isoStr)
			pack = ISO8583()
			#change the protocol
			pack.redefineBit(18, '18', 'Merchant Category Code', 'N', 4, 'n')
        		pack.redefineBit(60, '60', 'Additional Data', 'LLL', 999, 'ans')
        		pack.redefineBit(62, '62', 'Custom Data', 'AN', 26, 'ans')
			#parse the iso
			try:
				if bigEndian:
					pack.setNetworkISO(isoStr)
				else:
					pack.setNetworkISO(isoStr,False)
			
				v1 = pack.getBitsAndValues()
				for v in v1:
					print ('Bit %s of type %s with value = %s' % (v['bit'],v['type'],v['value']))
					bitmap = str(v['bit'])
					bittype = str(v['type'])
					bitvalue = str(v['value'])
					#print "The bit " , bitmap
					validate_ISO8583(bitmap, bittype, bitvalue)

				if pack.getMTI() == '0200':
					print ("\tThat's great !!! The client send a correct message !!!")
				else:
					print ("The client dosen't send the correct message!")	
					break
					
					
			except InvalidIso8583, ii:
				print ii
				break
			except:
				print ('Something happened!!!!')
				break
			
			#send answer
			auth_code = '000000'
			response_code = '00'
			response = ISO8583()
			response.setMTI('0210')
			#echoed from request
			response.setBit(2, pack.getBit(2))
			response.setBit(3, pack.getBit(3))
			response.setBit(4, pack.getBit(4))
			response.setBit(11, pack.getBit(11))
			response.setBit(12, pack.getBit(12))
			response.setBit(13, pack.getBit(13))
			#response.setBit(15, pack.getBit(15))
			response.setBit(18, pack.getBit(18))
			response.setBit(19, pack.getBit(19))
			response.setBit(32, pack.getBit(32))
			response.setBit(37, pack.getBit(37))
			
			#6 alpha numeric characters, fixed lentgh
			#Conditional  only present if the transaction is approved.  
			#If issuing bank does not approve the authorization, this field will not be present.
			response.setBit(38, auth_code); 
			response.setBit(39, response_code); 
			response.setBit(49, pack.getBit(49)); 
			
			if bigEndian:
				ans = response.getNetworkISO()
			else:
				ans = response.getNetworkISO(False)
				
			print ('Sending answer %s' % ans)
			connection.send(ans)
			
		else:
			break
	# close socket		
	connection.close()             
	print ("Closed...")



