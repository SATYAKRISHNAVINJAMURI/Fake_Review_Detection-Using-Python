from sys import *
import re
import nltk
from DataSet import DataSet

class SWN3:
	_dict = {}
	def __init__(self):
		self._pathToSWN = "/home/hduser1/workspace/dm_project/src/data/sentiword.txt"
		_temp = {}
		try:

			in_file = open(self._pathToSWN,"r")
			while True:
				in_line = in_file.readline()
				if not in_line:
					break
				data = in_line.split("\t")
				score = float(data[2]) - float(data[3])
				words = data[4].split(" ")
				for w in words:
					w_n = w.split("#")
					w_n[0] += "#" + data[0]
					index = int(w_n[1]) - 1
					if w_n[0] in _temp:
						v = _temp[w_n[0]]
						if index > len(v):
							for i in range(len(v),index):
								v.append(0.0)
						v.insert(index,score)
						_temp[w_n[0]] = v
					else:
						v = []
						for i in range(0, index):
							v.append(0.0)
						v.insert(index,score)
						_temp[w_n[0]] = v

			temp = _temp.keys()
			for word in temp:
				v = _temp[word]
				score = 0.0
				sum = 0.0
				b = 0.0
				for i in range(0,len(v)):
					b = v[i]
					if b != 0.0:
						score += float((1/(i+1))*v[i])
						sum += float(1/(i+1))
			if  sum != 0.0:
				score /= sum
			else:
				score = 0.0
			self._dict[word] = score
			in_file.close()
			print(self._dict)
		except IOError:
			print("Error in self")

	def classifyreview(self,tagged):
		total = 0
		totalScore = 0
		averageScore = 0
		i = 0
		tokenizer = nltk.word_tokenize(tagged)
		for word in tokenizer:
			if re.search("/V",word):
				all_words = word.split("/")
				if self.check_for_word(all_words[0]):
					word = all_words[0] + "#v"
					if word in self._dict.keys():
						total = self._dict[word] + total
						if self._dict[word] != 0:
							i = i+1

				else:
					all_words[0] = self.preprocessing(all_words[0])
					if self.check_for_word(all_words[0]):
						word = all_words[0] + "#v"
						if word in self._dict.keys():
							total = self._dict[word] + total
							if self._dict[word] != 0:
								i = i +1
			elif re.search("/J",word):
				all_words = word.split("/")
				if self.check_for_word(all_words[0]):
					word = all_words[0] + "#a"
					if word in self._dict.keys():
						total = self._dict[word] + total
						if self._dict[word] != 0:
							i = i+1

				else:
					all_words[0] = self.preprocessing(all_words[0])
					if self.check_for_word(all_words[0]):
						word = all_words[0] + "#a"
						if word in self._dict.keys():
							total = self._dict[word] + total
							if self._dict[word] != 0:
								i = i +1
			elif re.search("/R",word):
				all_words = word.split("/")
				if self.check_for_word(all_words[0]):
					word = all_words[0] + "#r"
					if word in self._dict.keys():
						total = self._dict[word] + total
						if self._dict[word] != 0:
							i = i+1

				else:
					all_words[0] = self.preprocessing(all_words[0])
					if self.check_for_word(all_words[0]):
						word = all_words[0] + "#r"
						if word in self._dict.keys():
							total = self._dict[word] + total
							if self._dict[word] != 0:
								i = i +1

			totalScore += total
			total = 0
		averageScore = totalScore/i
		return averageScore


	def check_for_word(self,word):
		try:
			in_file = open ("/usr/share/dict/american-english","r")
			while True:
				in_line = in_file.readline()
				if not in_line:
					break
				if word in in_line :
					return True
			in_file.close()
		except IOError:
			print("Error in Checking Word")
		return False


	def preprocessing(self,str):
		return str.replaceAll("(.)\\1{1,}", "$1")

	def main(self):
		print(self.check_for_word("hai"))

