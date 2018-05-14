from sys import *

class WordChecker(object):
	def check_for_word(self,word):
		try:
			in_file = open ("/usr/share/dict/american-english","r")
			while True:
				in_line = in_file.readline(in_file)
				if not in_line:
					break
				if in_line.indexOf(word) != -1 :
					return True
			in_file.close()
		except IOError:
			print("Error in Checking Word")
		return false

	def main(self):
		print(self.check_for_word("hai"))
