#Remember the countdown - timer program we created in chapter 8, Modify the program to use a variable loop.The Program should #ask the user where the countdown should start.

import time
countDown = int(raw_input("Where do you want the countdown to start = "))

for i in range(countDown,0,-1):
	print i
	time.sleep(1)
print "Blast off"
