# Fake_Review_Detection-Using-Python


Dataset:
Dataset can be downloaded from the following link:
https://drive.google.com/open?id=1-vMEbV1LXGiAN3NGGB-8rYu7W0ioF6zO


Complete Details about the Project are found in the following Document:
https://drive.google.com/open?id=109OWXzKFxBdl0KQnj_xYJO-2DRHE2Zd2


How to run the program:
	a) Download the DataSet file.
	b) Now get into the project directory.
	c) Use command $>>> python3 __main__.py <DataSet_path(absolute)>

How to determine the reviews is fake or genuine:
	a)Sentimental Score is generated for each review given to a product and it is reffered as calculated rating.
	b)Now based on the product name we calculate the average rating of the product by averaging all the ratings given by customer
	  to that particular product which is reffered as average rating.
	c)The Genuinness of the review can be determined by calculating the difference between average_rating and calculated_rating. If
	  the difference is greater then 0.5, review is said to be "Not Genuine"
	

Example: If a review  "r" is written for a product_name "x" by an user. First we calculate the sentimental score of the review "y" which is
reffered as calculated rating and then we average all the ratings given by several other users to the product "x" which is reffered as
average rating. 


How to Understand the Several String Comparision made:
	a)One can get a clear understanding about the string comparision made after having a look at DataSet. The DataSet is obvious and 
          contains redundant data which is filtered using string comparisions.

String comparisions in SWN3:
	a)Basic Understating
	b)Sentiword.net file is developed for calculating sentimental score of a word. It basically used to generates Sentimental Score.


Why more execution time:
	a)The average rating of the file needs to be calculated dynamically. So it has to go through entire DataSet to calculate the average_rating
	 which is a tedious task.This project is actually implemented in Map Reduce as it involves working with Big Data.

	 
	
