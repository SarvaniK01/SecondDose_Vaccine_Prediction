# The program is for checking when to take the second dose of covishield vaccine 
from datetime import date, timedelta, datetime
import calendar

print("**********The 2nd Dose of COVISHIELD vaccine can be taken BETWEEN 28 DAYS to 84 DAYS AFTER taking the FIRST DOSE**********")
print("\n")

# taking the input from the user
print("Enter numbers for date, month, year:")
dd = int(input("Enter the date you took the first vaccine(dd):"))
mm = int(input("Enter the month you took the first vaccine(mm):"))
yyyy = int(input("Enter the year you took the first vaccine(yyyy):"))

# specify the start date
start_date = date(yyyy,mm,dd)

print("\n")
twenty_eight_days = start_date + timedelta(days=28)
# print("28 Days:",twenty_eight_days)

eighty_four_days = start_date + timedelta(days=84)
# print("84 days:", eighty_four_days)

last_date = start_date + timedelta(days = 112)
# print("Last date:", last_date)
# 2 months 24 days

#changing the format of the date  
twenty_eight_days1 = date.strftime(twenty_eight_days,format="%d %B %Y")
eighty_four_days1 = date.strftime(eighty_four_days, format="%d %B %Y")
last_date1 = date.strftime(last_date,format = "%d %B %Y")

# printing the dates
print("\n")
print("You can take the SECOND DOSE of VACCINE")
print("FROM (with gap of 28 days):", str(twenty_eight_days1))
print("TO (with gap of 84 days):", str(eighty_four_days1))
print("\n")
print("But you have to take your second dose of vaccine BEFORE(112 days):", str(last_date1))

