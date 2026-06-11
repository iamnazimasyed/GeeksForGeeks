#User function Template for python3
# Take year input and print if year is a leap year
year = int(input())
print(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))
