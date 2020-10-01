import time as t
time_now = t.localtime()

print ("completed at ", str(time_now.tm_hour) + "H" + str(time_now.tm_min) + "M")

# Arithmatic with t.time to add 7 days to the current_time. 86400 is num of seconds in 1 day.
current_time = t.time()
delivery_time = current_time + (86400 * 7)
print(t.localtime(delivery_time))

# creates a 5 second wait between lines of code.
t.sleep(5)





