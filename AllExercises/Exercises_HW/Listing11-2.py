#Take a program you wrote in question #1, and have it print a row of stars beside each number like this

"""condown timer:how many seconds?4
4 ****
3 ***
2 **
1 *
"""

import time
countDown = int(raw_input("Where do you want the countdown to start = "))

for countdown in range(countDown,0,-1):
	print countdown,
	for star in range(countdown):
		print "*",
	print
	time.sleep(1)
print "Blast off"
