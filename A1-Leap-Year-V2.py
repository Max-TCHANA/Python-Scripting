#this program allows to verify is a year given by a user is a leap year 
import os
year = input("Please enter a year: ") #we invite the user to enter a year
#we convert input provided by the user into integer
year = int(year) #an error could happen is the user does not provide an integer
#Here we start the analysis to identify if the year is a leap year or not. Assuming that the user provided an appropriate value

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

os.system("pause")