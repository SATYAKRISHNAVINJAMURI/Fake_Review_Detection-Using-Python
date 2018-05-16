
import re
import nltk 


class SWN3:
	'''This class is an implementation of couple of modules which
are useful to calculate Sentiment Score of a Review. '''


    __pathtoSWN = "./resources/sentiwords.txt"
    _dict = {}

    def __init__(self):
''' This method initiallizes all the words as provides in the sentiword.txt file
in a dictionary variable which is used for calculating Sentimental Score 
for a Review.'''
        _temp = {}
        try:
            in_file = open(self.__pathtoSWN, "r")
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
                    if w_n[0] in _temp.keys():
                        v = _temp[w_n[0]]
                        if index > len(v):
                            for i in range(len(v), index):
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
                summ = 0.0
                for i in range(0, len(v)):
                    b = v[i]
                    if b != 0.0:
                        score += (1/(i+1)) * v[i]
                        summ += (1/(i+1))
                if summ != 0.0:
                    score /= summ
                else:
                    score = 0.0
                self._dict[word] = score
            in_file.close()
        except IOError:
            print("IOError in SWN3")

    def classifyreview(self,tagged):
''' This module help in calculating the Sentimental Score by using the
Sentiword.net file which is a conventional way to find the sentiment
score and uses all the words to generate a normalized rating on a scale
of -1 to 1'''
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
                                i = i + 1
            elif re.search("/J", word):
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
''' Check for a word in english dictionary and returns a Boolean value.'''
        try:
            in_file = open ("./resources/american-english","r")
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

    def preprocessing(self, str):
'''Text Preprocessing - Returns a word with single letter if a 
multiple letter word is given as an argument'''
        return str.replace("(.)\\1{1,}", "$1")

    def main(self):
        print(self.check_for_word("hai"))

