from sys import *

class DataSet(object):
    __pathtoreviewset = ""
    def __int__(self):
        self__pathtoreviewset = "/home/hduser1/workspace/dm_project/src/data/amazon_mp3"
    def calAverageRating(self,name):
        normalise = 0.0
        try:
            in_file= open(self.__pathtoreviewset,"r")
            line = ""
            i = 0
            dummy = ""
            rating = 0.0
            while True:
                in_line = in_file.readline(in_file)
                if not in_line:
                    break
                data = in_line.split(":")
                if data[0] == "[productName]":
                    dummy = data[1]
                    if data[1] == name:
                        i += 1
                if data[0] == "[rating]":
                    if dummy == name:
                        rating += float(data[1])

            normalise = ((((rating/i)*2)/5)-1)
            in_file.close()
            return normalise
        except RuntimeError:
            print("Error at Runtime in Calculating Average")