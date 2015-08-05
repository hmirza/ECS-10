#This program will test whether or not the inputted year is a leap year or not.

year = int(input("Please enter a year: "))

#The below statement tests whether or not the year is (a leap year) divisible by
#4, not divisible by 100,or divisble by 100 and 400

if year % 4 == 0 and (year %100 != 0 or year % 100 == 0 and year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year")

#Once tested, it will display the result



