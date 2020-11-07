import time
import datetime
import calendar 

week_days = ["Monday","Tuesday","Wednesday","Thursday"]
friday = "Friday"
week_ends = ["Saturday","Sunday"]
current_day = datetime.date.today().strftime("%A")
currunt_time = datetime.datetime.now().time()
time = "15:00:00"
current_date = datetime.datetime.now().date()
#print(day)
#print(time)
#print(current_date)
delivery_count = 0


def add_day(current_date):
	days = delivery_count
	delivery_date = datetime.datetime.now() + datetime.timedelta(days)
        delivery_day = datetime.datetime.strptime(delivery_date, '%Y %m %d').weekday()
	return (calendar.day_name[delivery_day]) 

#weekdays delivery date

for i in range(len(week_days)): 
	if(current_day==week_days[i])
		delivery_count = 1
    		#increment_Function
	elif(current_day==friday and current_time <= time )
        	delivery_count = 3
		#increment_Function
	elif(current_day==friday and current_time > time)
		delivery_count = 4
        	        
#weekends delivery date

	if(current_day==week_ends[i])
		delivery_count=3
		#increment_Function

	elif(current_day==week_ends[1])
		delivery_count=2
		#increment_Function



