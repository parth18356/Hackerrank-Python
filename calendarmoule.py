import datetime 
date=str(input())
day_name= ['MONDAY', 'TEUSDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY','SUNDAY']
day = datetime.datetime.strptime(date, '%m %d %Y').weekday()
print(day_name[day])
