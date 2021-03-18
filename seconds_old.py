# Calculate the number of seconds since you were born if you're into that..
import datetime

# Get the current time to subtract from
now = datetime.datetime.now()

# Set the date/time you were born **not my birthday**
year = 2000
month = 4
day = 20
hour = 6
minute = 30
birth = datetime.datetime(year, month, day, hour, minute)

print(f'\n-------------------------------------'
      f'\nToday: {now}\n'
      f'\n(minus)\n'
      f'\nBirth: {birth}'
      f'\n-------------------------------------')

# Timedelta object created when difference is taken between now and birth 
# Call '.total_seconds()' on timedelta object to calculate the total seconds in that interval 
time_delter = (now - birth)
print(f'\n\t*** Total Seconds Alive: {time_delter.total_seconds()} ***')
