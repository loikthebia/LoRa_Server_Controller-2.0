#!/bin/python2.7
# coding=utf-8

import sys
from database import Database


class Gateway():

	def __init__(self, eui):
		self.eui = eui
		self.exist = False

		db = Database("lora_network")
		if db is not None:
			result = db.query("SELECT * FROM gateways WHERE eui="+str(int(self.eui, 16)))
			if result is not None:
				self.exist = True
				self.region = result[0][1]
				self.maxTxPower_dBm = result[0][2]
				self.allowGpsToSetPosition = result[0][3]
				self.time = result[0][4]
				self.latitude = result[0][5]
				self.longitude = result[0][6]
				self.altitude = result[0][7]
				self.ntwkMaxDelayUp_ms = result[0][8]
				self.ntwkMaxDelayDn_ms = result[0][9]
				self.uppacketsreceived = result[0][10]
				self.gooduppacketsreceived = result[0][11]
				self.uppacketsforwarded = result[0][12]
				self.uppacketsacknowedgedratio = result[0][13]
				self.downpacketsreceived = result[0][14]
				self.packetstransmitted = result[0][15]
				self.lastuppacketid = result[0][16]
				self.dspVersion = result[0][17]
				self.fpgaVersion = result[0][18]
				self.halVersion = result[0][19]


	def add_cmd(self):
		command = "ns\n"
		if not self.exist:
			command = "gateway add "+str(self.eui)
		else:
			command = "gateway set "+str(self.eui)
		if self.region is not None:
			if self.region == 0:
				command = command+" region americas902"
			elif self.region == 1:
				command = command+" region china779"
			elif self.region == 2:
				command = command+" region europe433"
			elif self.region == 4:
				command = command+" region europe863"
		if self.latitude is not None:
			command = command+" lat "+str(self.latitude)
		if self.longitude is not None:
			command = command+" long "+str(self.longitude)
		if self.altitude is not None:
			command = command+" alt "+str(self.altitude)
		if self.allowGpsToSetPosition is not None:
			if self.allowGpsToSetPosition == True:
				command = command+" allowgps true"
			else:
				command = command+" allowgps false"
		if self.maxTxPower_dBm is not None:
			command = command+" pwr "+str(self.maxTxPower_dBm)
		if self.ntwkMaxDelayUp_ms is not None:
			command = command+" updelay_ms "+str(self.ntwkMaxDelayUp_ms)
		if self.ntwkMaxDelayDn_ms is not None:
			command = command+" downdelay_ms "+str(self.ntwkMaxDelayDn_ms)+"\n"
		return command


	def del_cmd(self):
		if not self.exist:
			pass
		else:
			command = "ns\ngateway delete "+str(self.eui)+"\n"
			return command


	def getregion(self):
		return self.region
	def getmaxTxPower_dBm(self):
		return self.maxTxPower_dBm
	def getallowGpsToSetPosition(self):
		return self.allowGpsToSetPosition
	def gettime(self):
		return self.time
	def getlatitude(self):
		return self.latitude
	def getlongitude(self):
		return self.longitude
	def getaltitude(self):
		return self.altitude
	def getntwkMaxDelayUp_ms(self):
		return self.ntwkMaxDelayUp_ms
	def getntwkMaxDelayDn_ms(self):
		return self.ntwkMaxDelayDn_ms
	def getuppacketsreceived(self):
		return self.uppacketsreceived
	def getgooduppacketsreceived(self):
		return self.gooduppacketsreceived
	def getuppacketsforwarded(self):
		return self.uppacketsforwarded
	def getuppacketsacknowedgedratio(self):
		return self.uppacketsacknowedgedratio
	def getdownpacketsreceived(self):
		return self.downpacketsreceived
	def getpacketstransmitted(self):
		return self.packetstransmitted
	def getlastuppacketid(self):
		return self.lastuppacketid
	def getdspVersion(self):
		return self.dspVersion
	def getfpgaVersion(self):
		return self.fpgaVersion
	def gethalVersion(self):
		return self.halVersion

	def setregion(self, region):
		self.region = region
	def setmaxTxPower_dBm(self, maxTxPower_dBm):
		self.maxTxPower_dBm = maxTxPower_dBm
	def setallowGpsToSetPosition(self, allowGpsToSetPosition):
		self.allowGpsToSetPosition = allowGpsToSetPosition
	def setlatitude(self, latitude):
		self.latitude = latitude
	def setlongitude(self, longitude):
		self.longitude = longitude
	def setaltitude(self, altitude):
		self.altitude = altitude
	def setntwkMaxDelayUp_ms(self, ntwkMaxDelayUp_ms):
		self.ntwkMaxDelayUp_ms = ntwkMaxDelayUp_ms
	def setntwkMaxDelayDn_ms(self, ntwkMaxDelayDn_ms):
		self.ntwkMaxDelayDn_ms = ntwkMaxDelayDn_ms



class Mote():

	def __init__(self, eui):
		self.eui = eui
		self.exist = False

		db = Database("lora_network")
		if db is not None:
			result = db.query("SELECT * FROM motes WHERE eui="+str(int(self.eui, 16)))
			if result is not None:
				self.exist = True
				self.appeui = str(int(result[0][1], 16))
				self.classC = result[0][2]
				self.networkAddress = str(int(result[0][3], 16))
				self.networkSessionKey = result[0][4]
				self.downMsgSeqNo = result[0][5]
				self.upMsgSeqNo = result[0][6]

		db = Database("lora_application")
		if db is not None:
			result = db.query("SELECT * FROM activemotes WHERE eui="+str(int(self.eui, 16)))
			if result is not None:
		self.applicationSessionKey = result[0][3]


	def add_cmd():
		command = "as\n"
		if not self.exist:
			command = "mote add "+str(self.eui)
		else:
			command = "mote set "+str(self.eui)
		command = command+" p app "+str(self.appeui)
		if self.networkAddress is not None:
			command = command+" netaddr "+str(self.networkAddress)+" key"
		if self.applicationSessionKey is not None:
			command = command+" "+str(self.applicationSessionKey)
		if not self.exist:
			command = command+"\nnc\nmote add "+str(self.eui)+" app "+str(self.appeui)+"\n"
			command = command+"cs\nmote add "+str(self.eui)+" app "+str(self.appeui)+"\n"
		else:
			command = command+"\nnc\nmote set "+str(self.eui)+" app "+str(self.appeui)+"\n"
			command = command+"cs\nmote set "+str(self.eui)+" app "+str(self.appeui)+"\n"
		if not self.exist:
			command = command+"ns\nmote add "+str(self.eui)+" app "+str(self.appeui)
		else:
			command = command+"ns\nmote set "+str(self.eui)+" app "+str(self.appeui)
		if self.networkSessionKey is not None:
			command = command+" key "+str(self.networkSessionKey)
		if self.networkAddress is not None:
			command = command+" netaddr "+str(self.networkAddress)
		if self.classC != 0:
			command = command+" class c\n"
		return command


	def del_cmd(self):
		if not self.exist:
			pass
		else:
			command = "as\nmote delete "+str(self.eui)+"\nnc\nmote delete "+str(self.eui)+"\nns\nmote delete "+str(self.eui)+"\ncs\nmote delete "+str(self.eui)+"\n"
			return command


	def geteui(self):
		return self.eui
	def getappeui(self):
		return self.appeui
	def getexist(self, exist):
		return self.exist
	def getclassC(self):
		return self.classC
	def getnetworkAddress(self):
		return self.networkAddress
	def getnetworkSessionKey(self):
		return self.networkSessionKey
	def getdownMsgSeqNo(self):
		return self.downMsgSeqNo
	def getupMsgSeqNo(self):
		return self.upMsgSeqNo
	def getapplicationSessionKey(self):
		return self.applicationSessionKey

	def setappeui(self, appeui):
		self.appeui = appeui
	def setclassC(self, classC):
		self.classC = classC
	def setnetworkAddress(self, networkAddress):
		self.networkAddress = networkAddress
	def setnetworkSessionKey(self, networkSessionKey):
		self.networkSessionKey = networkSessionKey
	def setapplicationSessionKey(self, applicationSessionKey):
		self.applicationSessionKey = applicationSessionKey



class App():

	def __init__(self, eui):
		self.eui = eui
		self.exist = False

		db = Database("lora_network")
		if db is not None:
			result = db.query("SELECT * FROM motes WHERE eui="+str(int(self.eui, 16)))
			if result is not None:
				self.exist = True
				self.name = result[0][1]
				self.owner = result[0][2]


	def add_cmd():
		if not self.exist:
			command = "ns\napp add "+str(self.eui)+" "+str(self.name)+" "+str(self.owner)+"\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipas)+" active user motetx gwrx joinserver maccmd\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipnc)+" active motetx gwrx maccmd\n"
			command = "as\napp add "+str(self.eui)+" "+str(self.name)+" "+str(self.owner)+"\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipcs)+" active user motetx gwrx joinmonitor maccmd\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipns)+" passive downstream\n"
			command = "cs\napp add "+str(self.eui)+" "+str(self.name)+" "+str(self.owner)+"\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipas)+" passive downstream\n"
			command = "nc\napp add "+str(self.eui)+" "+str(self.name)+" "+str(self.owner)+"\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipcs)+" active user\n"
			command = command+"app server add "+str(self.eui)+" "+str(self.ipns)+" passive downstream\n"
			return command


	def del_cmd():
		if not self.exist:
			pass
		else:
			command = "as\napp delete "+str(self.eui)+"\nnc\napp delete "+str(self.eui)+"\nns\napp delete "+str(self.eui)+"\ncs\napp delete "+str(self.eui)+"\n"
			return command


	def geteui(self):
		return self.eui
	def getexist(self):
		return self.exist
	def getname(self):
		return self.name
	def getowner(self):
		return self.owner

	def seteui(self, eui):
		self.eui = eui
	def setname(self, name):
		self.name = name
	def setowner(self, owner):
		self.owner = owner
