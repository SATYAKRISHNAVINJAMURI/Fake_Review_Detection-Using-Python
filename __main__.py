from sys import *
import re

class Main(object):
	_product_name = ""
	_rating = 0.0
	_review = ""
	_cal_rating = 0.0
	_avg_rating = 0.0
	_review_id = 0;
	_pathtoreviewset = ""

	def threshold(self,x,y):
		value = 0.0
		value = x-y
		if value < 0:
			return -value
		else:
			return value
	def main(self):
		samp = SWN3()
		ds = Dataset(pathtoreviewset)
		tagger - new MaxentTagger()"/home/hduser1/workspace/dm_project/src/data/left3words-wsj-0-18.tagger")
		try:
			in_file = open(self._pathtoreviewset)
			line = ""
			while True:
				in_line = in_file.readline(in_file)
				if not in_line:
					break
				data = in_line.split(":")
				if re.search(data[0],"^#{5}(.*)"):
					id = line.split("^#{5}")
					review_id = int(id[1])
					print("\n\n\nFor Review" + review_id)
				elif data[0] == "[productName]"
					product_name = data[1]
				elif data[0] == "[fullText"
					review = data[1]
					review = review.lower()
					tagged = tagger.tagString(review)
					cal_rating = samp.classifyreview(tagged)
					avg_rating = ds.calAverageRating(product_name)
				elif data[0].equals("[rating]"):
					rating = float(data[1])
					rating = (((rating/5)*2 )-1)
					print("Calculated rating: " + cal_rating)
					print("Average Rating: " + avg_rating)
					if not self.threshold(avg_rating,cal_rating) < 0.5
						print("NOt a Genuine Review.")
					else:
						print("Genuine Review")
			in_line.close()
		except IOError:
			print("ERROR in main")


