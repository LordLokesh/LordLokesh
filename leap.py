a=int(input("enter the year:"))
if a%4==0 and a%100!=0 or a%400==0:
    print("leapyear")
else :
    print("not a leap year")
