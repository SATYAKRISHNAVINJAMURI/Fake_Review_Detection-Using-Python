class DataSet:
    """ This class is defined on the dataSet which requires a dataset
    to be passed as an argument"""
    
    def __init__(self, file):
        self.__path_to_review_set = file

    def cal_average_rating(self, name):
        """ Calculate average rating of that product by adding up all
        the ratings of the product and taking an average"""
        try:
            in_file = open(self.__path_to_review_set, "r")
            i = 0
            dummy = ""
            rating = 0.0
            while True:
                in_line = in_file.readline()
                if not in_line:
                    break
                data = in_line.split(":")
                if data[0] == "[productName]":
                    dummy = data[1]
                    if dummy == name:
                        i += 1
                if data[0] == "[rating]":
                    if dummy == name:
                        rating += float(data[1])

            normalise = ((((rating/i)*2)/5)-1)
            in_file.close()
            return normalise
        except RuntimeError:
            print("Error at Runtime in Calculating Average")
