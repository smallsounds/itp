monthNumber = int(input("Please enter a month's number for its corresponding season."))

if monthNumber < 1 or monthNumber > 12:
    print("There are only 12 months in a year.")
elif monthNumber < 4 or monthNumber > 11:
    print("Boston is in Winter")
elif monthNumber > 3 and monthNumber < 7:
    print("Boston is in Spring")
elif monthNumber > 6 and monthNumber < 10:
    print("Boston is in Summer")
elif monthNumber > 9 and monthNumber < 12: 
    print("Boston is in Autumn")
