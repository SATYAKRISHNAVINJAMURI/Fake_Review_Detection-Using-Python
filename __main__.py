import re
import DataSet
import SWN3
import nltk


class Main(object):
	_product_name = ""
	_review = ""
	_cal_rating = 0.0
	_avg_rating = 0.0
	_review_id = 0
	_pathtoreviewset = ""

	def threshold(self,x,y):
		value = x-y
		if value < 0:
			return -value
		else:
			return value
	def main(self):
		try:
			in_file = open(self._pathtoreviewset)
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
				elif data[0] == "[fullText":
					review = data[1]
					review = review.lower()
					tokenized = nltk.word_tokenizer(review)
					tagger = nltk.pos_tag(tokenized)
					tagged = ""
					for element in tagger:
						tagged += " " + element[0] +"/" + element[1]
					cal_rating = SWN3.classifyreview(tagged)
					avg_rating = DataSet.calAverageRating(product_name)
				elif data[0].equals("[rating]"):
					rating = float(data[1])
					rating = (((rating/5)*2 )-1)
					print("Calculated rating: " + cal_rating)
					print("Average Rating: " + avg_rating)
					if not self.threshold(avg_rating,cal_rating) < 0.5:
						print("NOt a Genuine Review.")
					else:
						print("Genuine Review")
			in_file.close()
		except Exception as err:
			print(str(err))


