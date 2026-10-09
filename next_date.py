day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

# Leap year
if year % 400 == 0:
    leap = True
elif year % 100 == 0:
    leap = False
elif year % 4 == 0:
    leap = True
else:
    leap = False

# Days in month
if month == 2:
    if leap:
        days = 29
    else:
        days = 28

elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30

elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31

else:
    days = 0

# Validation
if year <= 0 or month < 1 or month > 12 or day < 1 or day > days:
    print("Invalid date")

else:

    if day < days:
        day = day + 1

    else:
        day = 1

        if month < 12:
            month = month + 1
        else:
            month = 1
            year = year + 1

    print("Next date:", day, "/", month, "/", year)