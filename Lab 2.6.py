Lab 2.6.11
hour = int(input("Starting time (hours): 12 "))
mins = int(input("Starting time (minutes): 58 "))
dura = int(input("Event duration (minutes): 1 "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')