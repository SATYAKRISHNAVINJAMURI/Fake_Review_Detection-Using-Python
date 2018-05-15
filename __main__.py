import re
from DataSet import DataSet
from SWN3 import SWN3
import nltk


class Main:
	_product_name = ""
	_review = ""
	_cal_rating = 0.0
	_avg_rating = 0.0
	_review_id = 0
	_pathtoreviewset = "/home/satya/dm_project/src/data/data1.txt"

	def threshold(self,x,y):
		value = x-y
		if value < 0:
			return -value
		else:
			return value
	def detect(self):
		samp = SWN3()
		ds = DataSet()
		try:
			in_file = open(self._pathtoreviewset,"r")
			line = ""
			while True:
				in_line = in_file.readline()
				if not in_line:
					break
				data = in_line.split(":")
				if re.search(data[0],"^#{5}(.*)"):
					id = line.split("^#{5}")
					review_id = int(id[1])
					print("\n\n\nFor Review" + review_id)
				elif data[0] == "[productName]":
					product_name = data[1]
				elif data[0] == "[fullText]":
					review = data[1]
					review = review.lower()
					tokenized = nltk.word_tokenize(review)
					tagger = nltk.pos_tag(tokenized)
					tagged = ""
					for element in tagger:
						tagged += " " + element[0] +"/" + element[1]
					cal_rating = samp.classifyreview(tagged)
					avg_rating = ds.calAverageRating(product_name)
					print("Calculated rating: " + str(cal_rating))
					print("Average Rating: " + str(avg_rating))
					if not self.threshold(avg_rating, cal_rating) < 0.5:
						print("NOt a Genuine Review.")
					else:
						print("Genuine Review")

			in_file.close()
		except IOError:
			print("IOERROR in main")

m = Main()
m.detect()



