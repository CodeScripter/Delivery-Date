from datetime import datetime, date
from datetime import timedelta
from datetime import datetime
import time
import datetime
import calendar 

week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
current_day = datetime.date.today().strftime("%A")
current_time = str(datetime.datetime.now().time())
time = "15:00:00"
current_date = date.today()
delivery_count = 0
def add_day(current_date):
	delevery_date = current_date + timedelta(delivery_count)
	delivery_day = datetime.datetime.strptime(str(delevery_date), '%Y-%m-%d').weekday() 
	return (calendar.day_name[delivery_day])
    
for i in range(len(week)):
    if current_day == week[0] or current_day == week[1] or current_day == week[2] or current_day == week[3]:
        delivery_count = 1
        print("Day of order:- ",current_day)
        print("Date of order:- ",current_date)
        print("Day of the delivery:- ",add_day(current_date))
        print("date of the delivery:- ",current_date + timedelta(delivery_count))
        break
    elif current_day == week[4] and current_time <= time:
        delivery_count = 3
        print("Day of order:- ",current_day)
        print("Time of thr day:- ",current_time)
        print("Date of order:- ",current_date)
        print("Day of the delivery:- ",add_day(current_date))
        print("date of the delivery:-",current_date + timedelta(delivery_count))
        break
    elif current_day == week[4] and current_time > time:
        delivery_count = 4
        print("Day of order:- ",current_day)
        print("Time of thr day:- ",current_time)
        print("Date of order:- ",current_date)
        print("Day of the delivery:- ",add_day(current_date))
        print("date of the delivery:-",current_date + timedelta(delivery_count))
        break
    elif current_day == week[5] or current_day == week[6]:
        delivery_count=3
        print("Day of order:- ",current_day)
        print("Date of order:- ",current_date)
        print("Day of the delivery:- ",add_day(current_date))
        print("date of the delivery:-",current_date + timedelta(delivery_count))
        break
    else:
        break

            
