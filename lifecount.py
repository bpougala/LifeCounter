# File: lifecount.py
# This short program in Python, when given a date of birth, computes the number of days, 
# hours, minutes and seconds we've been alive. 
# Copyright 2018 Biko Pougala. All rights reserved. 

import time 

def count(str): 
   day_   = str[0] + str[1]
   month_ = str[3] + str[4]
   year_  = str[6] + str[7] + str[8] + str[9]
   
   day = int(day_)
   month = int(month_)
   year_ = int(year_) 
   
   current_day   = time.strftime("%d")
   current_month = time.strftime("%m")
   current_year  = time.strftime("%Y")  # year with century as a decimal number  
   
   if (month %2 != 0 or month == 8 and day > 31): 
      print("Error: can't have more than 31 days in a month.")
   elif (month == 2 and year % 4 != 0 and day > 29):  # account for leap years 
      print("Error: can't have more than 29 days in February.")
   elif (month % 2 == 0 and month != 8 and day > 30 and month != 2):
      print("Error: can't have more than 30 days in this month.")   
   elif (month == 2 and year % 4 != 0 and day > 28): 
      print("Error: can't have more than 28 days in February.") 
   elif (day > current_day and month > current_month and year > current_month): 
      print("Error: you're not born yet!") 
   else: 
      age = current_year - year
      number_days = (age - 1) * 365 + age/4   # we add age/4 to account for leap years
      split = (12 - month)/2 
      if (month%2 == 0 and month != 2 and month != 8):
         remaning_days_1 = 30 - day
      elif (month%2 != 0 or month == 8): 
         remaining_days_1 = 31 - day
      elif (month == 2 and year%4 == 0):
         remaining_days_1 = 29 - day
      elif (month == 2 and year % 4 != 0): 
         remaining_days_1 = 28 - day 
      elif (month == 8): 
         remaining_days_1 = 31 - day
      if (month%2 == 0 and month < 8 and month > 2):  # July and August both have 31 days, hence special case
         remaining_days_1 += (split-1)*30 + (split+2)*31 
      elif (month == 2): 
         remaning_days_1 += 5 * 31 + 4 * 30
      elif (month%2 == 0 and month > 8): 
         remaining_days_1 += 30 * split + 31 * split 
      elif (month == 8): 
         remaining_days_1 += 2 * 30 + 2 * 31 
      elif (month%2 != 0 and month < 8):
         remaining_days_1 += split * 30 + (split + 1) * 31 
      elif (month%2 != 0 and month >= 8): 
         remaining_days_1 += split * 30 + (split + 1) * 31 
         
      # we've computed the number of days lived in our birth year 
      # we now need to compute the number of days lived in the current year 

      if (current_month %2 == 0 and current_month != 2 and current_year%4 != 0): 
          remaining_days_2 = 28 * 1 + 31 * (month/2) + 30 * (month - month/2 - 1) 
      elif (current_month %2 == 0 and current_month != 2 and current_year%4 == 0):
          remaining_days_2 = 29 * 1 + 31 * (month/2) + 30 * (month - month/2 - 1)
      elif (current_month == 2):
          remaining_days_2 = 31 + current_day 
      elif (current_month %2 != 0 and current_year %4 != 0): 
          remaining_days_2  = 28 * 1 + 31 * (month/2) + 30 * (month - month/2 - 1)
      elif (current_month %2 != 0 and current_year %4 == 0): 
          remaining_days_2 = 29 * 1 + 31 * (month/2) + 30 * (month - month/2 - 1)
          
      return day + remaining_days_1 + remaining_days_2  


def main(argv): 
   print("Enter your date of birth in format dd/mm/yyyy :")
   print(count(str(argv)))
   
   
  
if __name__ == "__main__":
   main(sys.argv[1:])