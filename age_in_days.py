""" project for final week done with basic course """
import datetime 
# would help in finding no.of days
def days_in_month(yeara,montha):    
    if(montha==2 and yeara%4==0):
        days=29
    elif(montha==2 and yeara%4!=0):
        days=28
    elif(montha<=7 and montha%2 !=0):
        days=31
    elif(montha<=7 and montha%2 ==0):
        days=30
    elif(montha>7 and montha%2 ==0):
        days=31
    else:
        days=30
    return days 
def is_valid_date(yearb,monthb,dateb): # help in checking a valid date
     
    if( 1<=yearb<=9999)and(1<=monthb<=12)and(1<=dateb <= days_in_month(yearb,monthb)):
        return True
    else :
        return False
def days_between(year,month,date,year1,month1,date1):
    # help in checking a valid date
    if(is_valid_date(year,month,date))and(is_valid_date(year1,month1,date1)) : 
        difference=0
    else :
        return 0
    date11=datetime.date(year,month,date)
    date22=datetime.date(year1,month1,date1)
    difference = date22-date11
    if(difference.days>0):
        return difference.days
    else:
        return 0 
def age_in_days(yearc,monthc,datec):
    # help in checking a valid date
    if(is_valid_date(yearc,monthc,datec)):
        difference=0
    else:
        return 0    
    todays_date=datetime.date.today()
    date33=datetime.date(yearc,monthc,datec)
    difference=todays_date-date33
    if(difference.days>0):
        age=difference.days
    else :
        age= 0
    return age