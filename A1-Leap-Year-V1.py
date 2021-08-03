#this program allows to verify if a year given by a user is a leap year 
import os
year = input("Please enter a year: ") #we invite the user to enter a year
#we convert input provided by the user into integer
year = int(year) #an error could happen is the user does not provide an integer
#Here we start the analysis to identify if the year is a leap year or not. Assuming that the user provided an appropriate value
if year%4 != 0:
    print(year, "is not a leap year")
else:
    if year%100 == 0:
        if year%400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")

os.system("pause")
