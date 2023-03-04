#Python programing essentials
'''
Problem 1: Computing the number of days in a month
Problem 2: Checking if a date is valid
Problem 3: Computing the number of days between two dates
Problem 4: Calculating a person's age in days
'''


import datetime
def days_in_month(year, month):

    #computing number of days in a month
    if (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1 <= month <=11):
        date1 = datetime.date(year,month,1)
        date2 = datetime.date(year,month+1,1)
        return (date2 - date1).days
    elif (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (month == 12):
        date1 = datetime.date(year,month,1)
        date2 = datetime.date(year+1,1,1)
        return (date2 - date1).days
    else:
        return False

def is_valid_date(year, month, day):

    days = days_in_month(year, month)
    if ((datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1<= month <= 12) and (0 < day <= days)):
        return True
    else:
        return False

def days_between(year1, month1, day1, year2, month2, day2):
 
   
    if (is_valid_date(year1, month1, day1)) and (is_valid_date(year2, month2, day2)):

        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)

        if (date2 > date1):
            number_of_days = date2 - date1
            return number_of_days.days
        else:
            return 0
    else:
        return 0
    

#computing person's age in days
def age_in_days(year, month, day):
    """
    Takes three integers as input(year,month,day) of a persons
    birthday and return that person's age in days as of today.
    """
    
    #conditions and calculations of person's age in days
    
    if (is_valid_date(year, month, day)):
        today = datetime.date.today()
        person_bday = datetime.date(year, month, day)
        if (person_bday < today):
            person_age_in_days = days_between(year, month, day, today.year, today.month, today.day)
            return person_age_in_days
        else:
            return 0
    else:
        return 0
