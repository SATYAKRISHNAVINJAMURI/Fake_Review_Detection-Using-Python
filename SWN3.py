from sys import *
import re

class SWN3(object):
	_dict = {}
	def __init__(self):
		self._pathToSWN = "/home/hduser1/workspace/dm_project/src/data/sentiword.txt"
		_temp = {}
		try:
			in_file = open(self._pathToSWN,"r")
			line = ""
			while True:
				in_line = in_file.readline(in_file)
				if not in_line:
					break
				data = line.split("\t")
				score = float(data[2]) - float(data[3])
				words = data[4].split(" ")
				for w in words:
					w_n = w.split("#")
					w_n[0] += "#" + data[0]
					index = int(w_n[1]) - 1
					if _temp.__contains__(w_n[0]):
						v = _temp.get(w_n[0])
						if index > len(v):
							for i in range[len(v),index]:
								v.add(0.0)
						v.add(index,score)
						_temp.put(w_n[0],v)
					else:
						for i in range[0, index]:
							v.add(0.0)
						v.add(index,score)
						_temp.put(w_n[0],v)

			temp = _temp.keySet()
			for word in temp:
				v = _temp.get(word)
				score = 0.0
				sum = 0.0
				b = 0.0
				for i in range[0,len(v)]:
					b = v.get(i)
					if b != 0.0:
						score += float((1/(i+1))*v.get(i))
						sum += float(1/(i+1))
			if  sum != 0.0:
				score /= sum
			else:
				score = 0.0
			SWN3._dict.put(word,score)
			in_file.close()
		except IOError:
			print("Error in SWN3")

	def classifyreview(tagged):
		total = 0
		totalScore = 0
		averageScore = 0
		i = 0
		tokenizer = StringTokenizer(tagged)
		for word in tokenizer:
			if re.search(word,"(.*)/V(.*)"):
				all_words = word.split("/")
				if SWN3.check_for_word(all_words[0]):
					word = all_words[0] + "#v"
					if SWN3._dict.get(word) != None:
						total = SWN3._dict.get(word) + total
						if SWN3._dict.get(word) != 0
							i = i+1

				else:
					all_words[0] = SWN3.preprocessing(all_words[0])
					if SWN3.check_for_word(all_words[0]):
						word = all_words[0] + "#v"
						if SWN3._dict.get(word) != None:
							total = SWN3._dict.get(word) + total
							if SWN3._dict.get(word) != 0:
								i = i +1
			elif re.search(word,"(.*)/J(.*)"):
				all_words = word.split("/")
				if SWN3.check_for_word(all_words[0]):
					word = all_words[0] + "#a"
					if SWN3._dict.get(word) != None:
						total = SWN3._dict.get(word) + total
						if SWN3._dict.get(word) != 0
							i = i+1

				else:
					all_words[0] = SWN3.preprocessing(all_words[0])
					if SWN3.check_for_word(all_words[0]):
						word = all_words[0] + "#a"
						if SWN3._dict.get(word) != None:
							total = SWN3._dict.get(word) + total
							if SWN3._dict.get(word) != 0:
								i = i +1
			elif re.search(word,"(.*)/R(.*)"):
				all_words = word.split("/")
				if SWN3.check_for_word(all_words[0]):
					word = all_words[0] + "#r"
					if SWN3._dict.get(word) != None:
						total = SWN3._dict.get(word) + total
						if SWN3._dict.get(word) != 0
							i = i+1

				else:
					all_words[0] = SWN3.preprocessing(all_words[0])
					if SWN3.check_for_word(all_words[0]):
						word = all_words[0] + "#r"
						if SWN3._dict.get(word) != None:
							total = SWN3._dict.get(word) + total
							if SWN3._dict.get(word) != 0:
								i = i +1

			totalScore += total
			total = 0
		averageScore = totalScore/i
		return averageScore


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
		return False


	def preprocessing(self,str):
		str.replaceAll("(.)\\1{1,}", "$1")
	def main(self):
		print(self.check_for_word("hai"))


print(SWN3.check_for_word(SWN3(),"super"))