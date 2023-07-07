import time
import random

timeAlloted = 60
start_time = time.time()

time.sleep(5)

end_time = time.time()

timeTaken = int(end_time - start_time)
# timeTaken = 62

forSleep = timeAlloted - timeTaken

print(forSleep)

if forSleep < 0:
  print("sleep is 0")
else:
  print(forSleep)


# print("Duration in seconds:", timeTaken)