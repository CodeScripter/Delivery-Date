import time
import datetime
import calendar 

week_days = ["Monday","Tuesday","Wednesday","Thursday"]
friday = "Friday"
week_ends = ["Saturday","Sunday"]
current_day = datetime.date.today().strftime("%A")
currunt_time = str(datetime.datetime.now().time())
time = "15:00:00"
current_date = date.today()
#print(day)
#print(time)
#print(current_date)
delivery_count = 0


def add_day(current_date):
	days = delivery_count
	delevery_date = current_date + timedelta(days=2)
	delivery_day = datetime.datetime.strptime(str(delevery_date), '%Y-%m-%d').weekday() 
	return (calendar.day_name[delivery_day]) 

#weekdays delivery date

for i in range(len(week_days)): 
	if current_day == week_days[i]:
		delivery_count = 1
		print(add_day(current_date))
	elif current_day == friday and current_time <= time:
		delivery_count = 3
		print(add_day(current_date)) 
#increment_Function
		elif current_day == friday and current_time > time:	
		delivery_count = 4	
		print(add_day(current_date)) 
#weekends delivery date
	if current_day == week_ends[0]:
		delivery_count=3
		print(add_day(current_date))
#increment_Function
		elif current_day == week_ends[1]:
		delivery_count=2
		print(add_day(current_date)) 
#increment_Function



