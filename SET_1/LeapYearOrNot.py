while(1):
    year = int(input("Enter a year (enter 0 to exit) : "))
    if year == 0:
        print("EXITING...")
        break

    if((year%4==0 and year%100!=0) or year%400==0):
        print("%d is a leap year.\n"%year)
    else:
        print("%d is not a leap year.\n"%year)