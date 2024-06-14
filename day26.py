###########..........day15.work.............###############

#writing good morning, good afternoon good evening and good night using ifelse stmt
import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)

if(hour > 0 and hour < 12):
  print("goodmorning")
elif(hour >= 12 and hour < 17):
  print("good afternoon")
elif(hour >=17 and hour < 20):
  print("good evening")
else:
  print("good night")

# timestamp = int(time.strftime('%M'))
# print(timestamp)
# timestamp = int(time.strftime('%S'))
# print(timestamp)

# if (int(timestamp) < 12 and int(timestamp) > 4):
#   print("good morning")
# elif (int(timestamp) >= 12 and int(timestamp) < 16):
#   print("good afternoon")
# elif (int(timestamp) >= 16 and int(timestamp) < 20):
#   print("good evening")
# else:
#   print("good night")
