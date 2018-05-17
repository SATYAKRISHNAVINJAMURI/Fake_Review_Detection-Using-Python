from fake_review.Detector import Detector
import sys


def main():
    # print command line arguments
    if len(sys.argv) != 2:
        print("Please Give DataSet as an Argument\n" + "Correct Way to execute:\n python3 __main__.py <dataset>")
        exit(1)
    print("DataSet: " + sys.argv[1])
    obj = Detector(sys.argv[1])
    obj.detect()


if __name__ == "__main__":
    main()
