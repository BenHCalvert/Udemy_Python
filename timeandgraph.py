# Create a program to help the user learn to type faster. Give him a word and ask them to write it 5 times. Check how many seconds it takes to type the word each round.

# In the end, tell the user how many mistakes were made and show a char with the typing speed for each of the 5 rounds.
import time as t
import matplotlib.pyplot as plt
import math
time_now = t.localtime()
x = [1, 2, 3, 4, 5]

begin = False
while (begin == False):    
    start = input("This game will help you type fast. You will be given a sentence 5 times. The game will tell you how long it took for you to type the sentence each time. Are you ready to begin(y/n)? ")
    print(start)
    try:
        start = "y"
        # if len(start) > 1 or start > (-math.inf):
        #     print("Please enter y or n")
        #     continue
        # else:
            begin = True
    except:
        print("Please restart when you are ready to begin (y/n)")
    print(start)
   


print ("completed at ", str(time_now.tm_hour) + "H" + str(time_now.tm_min) + "M")

# Arithmatic with t.time to add 7 days to the current_time. 86400 is num of seconds in 1 day.
current_time = t.time()
delivery_time = current_time + (86400 * 7)
print(t.localtime(delivery_time))

# creates a 5 second wait between lines of code.
t.sleep(5)