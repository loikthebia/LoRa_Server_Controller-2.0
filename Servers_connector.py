#!/bin/python2.7
# coding=utf-8

import sys
import time
import subprocess
import shlex
from threading import Thread


class Timer(Thread):

	def __init__(self, process, timeout):
		Thread.__init__(self)
		self.timeout = timeout
		self.process = process


	def run(self):
		time.sleep(self.timeout)
		self.process.terminate()
		sys.exit(0)


class Connector():

	def __init__(self, ipNS, ipAS, ipCS, ipNC):
		self.ipNS = ipNS
		self.ipAS = ipAS
		self.ipCS = ipCS
		self.ipNC = ipNC
	

	def append(self, command, timeout):
		command_line = "../loracmd -ns "+str(self.ipNS)+" -as "+str(self.ipAS)+" -cs "+str(self.ipCS)+" -nc "+str(self.ipNC)
		args = shlex.split(command_line)
		process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		thread = Timer(process, timeout)
		thread.start()
		return process.communicate(command)