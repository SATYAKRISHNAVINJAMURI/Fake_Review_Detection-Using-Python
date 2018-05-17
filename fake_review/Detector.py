import re
import nltk
from fake_review.SWN3 import SWN3
from fake_review.DataSet import DataSet


class Detector:
    """Classifies a review based on the sentimental Score"""
    __product_name = ""
    __cal_rating = 0.0
    __avg_rating = 0.0
    __review_id = 0
    __path_to_review_set = ""

    def __init__(self, file):
        self.__path_to_review_set = file

    @staticmethod
    def threshold(x, y):
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
        ds = DataSet(self.__path_to_review_set)
        try:
            in_file = open(self.__path_to_review_set, "r")
            while True:
                in_line = in_file.readline()
                if not in_line:
                    break
                data = in_line.split(":")
                if re.match("#####", data[0]):
                    id_ = in_line.split("#####")
                    __review_id = int(id_[1])
                    print("\n\n\nFor Review" + str(__review_id))
                elif data[0] == "[productName]":
                    self.__product_name = data[1]
                elif data[0] == "[fullText]":
                    review = data[1]
                    review = review.lower()
                    tokenized = nltk.word_tokenize(review)
                    tagger = nltk.pos_tag(tokenized)
                    tagged = ""
                    for element in tagger:
                        tagged += " " + element[0] + "/" + element[1]
                    __cal_rating = samp.classify_review(tagged)
                    __avg_rating = ds.cal_average_rating(self.__product_name)
                    print("Calculated rating: " + str(__cal_rating))
                    print("Average Rating: " + str(__avg_rating))
                    if not self.threshold(__avg_rating, __cal_rating) < 0.5:
                        print("Not a Genuine Review.")
                    else:
                        print("Genuine Review")

            in_file.close()
        except IOError:
            print("IOERROR in main")



