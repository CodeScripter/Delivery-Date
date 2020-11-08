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
	days = delivery_count
	delivery_date = current_date + timedelta(delivery_count)
	print("delivery date and day:- ",delivery_date)
	delivery_day = datetime.datetime.strptime(str(delivery_date), '%Y-%m-%d').weekday() 
	return (calendar.day_name[delivery_day]) 

if current_day == week[0] or current_day == week[1] or current_day == week[2] or current_day == week[3]:
    delivery_count = 1
    print(add_day(current_date))
elif current_day ==  week[4] and current_time <= time:
    delivery_count = 3
    print(add_day(current_date))
elif current_day == week[4] and current_time > time:
    delivery_count = 4
    print(add_day(current_date))
elif current_day == week[5]:
    delivery_count=3
    print(add_day(current_date))
elif current_day == week[6]:
    delivery_count=2
    print(add_day(current_date))
else:
    print("Inside Else")
