// Conversion output is limited to 512 chars while you are signed out
// Please, sign in or register to get more...

from System import *
from System.Collections.Generic import *
from System.Collections import *
from System.IO import *

class SWN3(object):
	def __init__(self):
		self._pathToSWN = "/home/hduser1/workspace/dm_project/src/data/sentiword.txt"

	def find_rating(self):
		self.__dict = Hashtable[str, Nullable]()
		_temp = Hashtable[str, ArrayList]()
		try:
			csv = BufferedReader(FileReader(self._pathToSWN))
			line = ""
			while (line = csv.readLine()) != None:
				data = line.split("\t")
				s