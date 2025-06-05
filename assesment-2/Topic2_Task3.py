# Task 3: Checking if leap year
year = int(input("Enter Year: "))
if year%4 == 0:
    if year%100 == 0 and year%400 == 0:
        print(f"Year: {year} is leap year")
    elif year%100 ==0 and year%400 !=0:
        print(f"Year: {year} is not a leap year")
    else:2500
        print(f"Year: {year} is leap year")
else:        
    print(f"Year: {year} is not a leap year")
    