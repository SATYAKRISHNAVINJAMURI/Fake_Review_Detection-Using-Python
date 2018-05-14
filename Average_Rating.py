from sys import *


class Average_Rating(object):
    def __init__(self):
        self._pathToreviewset = "/home/hduser1/workspace/dm_project/src/data/data1.txt"

    def calAverageRating(self,name):
        normalize = 0.0
        i = 0
        rating = 0.0
        try:
            in_file = open(self._pathToreviewset, "r")
            while True:
                in_line = in_file.readline()
                if not in_line:
                    break
                data = in_line.split(":")
                if data[0] == "[productName]" :
                    dummy = data[1]
                    print(dummy)
                    if  dummy == name:
                        i = i+1
                if data[0] == "[rating]" :
                    if  dummy == name:
                        rating += float(data[1])
            normalise = ((((rating / i) * 2) / 5) - 1)
            in_file.close()
            print(normalise)
            return normalise
        except FileNotFoundError:
            print("ERROR - Coudn't found the dataset")
        except FileExistsError:
            print("ERROR - Coudn't found the dataset")



try:
    ar = Average_Rating()
    print("Executin main")
    Average_Rating.calAverageRating(ar,"Rio PMP 300 MP3 Player")
except FileNotFoundError:
    print("ERRRO - Couldn't find the file")
except IOError:
    print("ERROR - IOERROR")


