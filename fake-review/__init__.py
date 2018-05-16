import re
from DataSet import DataSet
from SWN3 import SWN3
import nltk


class Main:
"""Classifies a review based on the sentimental Score"""
	_product_name = ""
	_review = ""
	_cal_rating = 0.0
	_avg_rating = 0.0
	_review_id = 0
	_pathtoreviewset = "/home/satya/dm_project/src/data/data1.txt"

	def threshold(self,x,y):
""" Returns the magnitude of difference between two values"""
		value = x-y
		if value < 0:
			return -value
		else:
			return value
	def detect(self):
""" This module classifies a review based on the sentimental score:
if the difference between the average and calculated sentimental scroe 
is more than the threshold value that is 0.5 then the review is classified
as not genuine and genuine otherwise."""
		samp = SWN3()
		ds = DataSet()
		try:
			in_file = open(self._pathtoreviewset, "r")
			while True:
				in_line = in_file.readline()
				if not in_line:
					break
				data = in_line.split(":")
				if re.match("#####", data[0]):
					id = in_line.split("#####")
					_review_id = int(id[1])
					print("\n\n\nFor Review" + str(_review_id))
				elif data[0] == "[productName]":
					_product_name = data[1]
				elif data[0] == "[fullText]":
					review = data[1]
					review = review.lower()
					tokenized = nltk.word_tokenize(review)
					tagger = nltk.pos_tag(tokenized)
					tagged = ""
					for element in tagger:
						tagged += " " + element[0] +"/" + element[1]
					_cal_rating = samp.classifyreview(tagged)
					_avg_rating = ds.calAverageRating(_product_name)
					print("Calculated rating: " + str(_cal_rating))
					print("Average Rating: " + str(_avg_rating))
					if not self.threshold(_avg_rating, _cal_rating) < 0.5:
						print("Not a Genuine Review.")
					else:
						print("Genuine Review")

			in_file.close()
		except IOError:
			print("IOERROR in main")

m = Main()
m.detect()



