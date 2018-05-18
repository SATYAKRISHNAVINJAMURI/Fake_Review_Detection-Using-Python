import re
from pkg_resources import *
import nltk 


class SWN3:
    """This class is an implementation of couple of modules which
    are useful to calculate Sentiment Score of a Review. """

    __path_to_SWN = resource_filename("fake_review.resources", "sentiword.txt")
    __dict = {}
    __exist_instance = False

    def __init__(self):
        """This method initiallizes all the words as provides in the sentiword.txt file
        in a dictionary variable which is used for calculating Sentimental Score for a Review."""
        if not self.__exist_instance:
            self.__exist_instance = True
            _temp = {}
            try:
                in_file = open(SWN3.__path_to_SWN, "r")
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
                            v.insert(index, score)
                            _temp[w_n[0]] = v
                        else:
                            v = []
                            for i in range(0, index):
                                v.append(0.0)
                            v.insert(index, score)
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
                    self.__dict[word] = score
                in_file.close()
            except IOError:
                print("IOError in SWN3")

    def calculate_sentiment_score(self, tagged):
        """This module help in calculating the Sentimental Score by using the
        Sentiword.net file which is a conventional way to find the sentiment
        score and uses all the words to generate a normalized rating on a scale of -1 to 1"""
        score = 0
        total_score = 0
        i = 0
        tokenizer = nltk.word_tokenize(tagged)
        for tag_word in tokenizer:
            word = tag_word.split("/")
            if self.word_exists(word[0]):
                if re.match("V", word[1]):
                    score = self.get_score(word[0], "#v")
                    if score is not 0.0:
                        i += 1
                elif re.match("J", word[1]):
                    score = self.get_score(word[0], "#a")
                    if score is not 0.0:
                        i += 1
                elif re.match("R", word[1]):
                    score = self.get_score(word[0], "#r")
                    if score is not 0.0:
                        i += 1
            total_score += score
        average_setimental_score = total_score/i
        return average_setimental_score

    def get_score(self, word, tag):
        score = 0.0
        tag_word = word + tag
        if tag_word in self.__dict.keys():
            score = self.__dict[tag_word]
        return score

    @staticmethod
    def word_exists(word):
        """ Check for a word in english dictionary and returns a Boolean value."""
        try:
            in_file = open(resource_filename("fake_review.resources", "american-english"), "r")
            while True:
                in_line = in_file.readline()
                if not in_line:
                    break
                if word in in_line:
                    in_file.close()
                    return True
            in_file.close()
            return False
        except IOError:
            print("Error in Checking Word")


