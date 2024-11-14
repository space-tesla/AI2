# Q.1 Write a Python program to generate a calendar for the given month and year.

import calendar

def display_calendar(year, month):
    print(calendar.month(year, month))

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

display_calendar(year, month)



"""Output:
Enter year: 2024
Enter month (1-12): 11

   November 2024
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30"""