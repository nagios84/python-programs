#
#	Correct the errors (without adding any new lines) in the program below and then trace the output.
#	
#


for a in [1,2]:									
       	for b in range(1,3):			
            for c in range(1,3):		
			    print a,":",b,":",c	
			
		




#
#     Trace the output.
#	
#
#	The format of the trace must be as follows (upto 20 steps is sufficient) :
# 	     
#
#       Trace of the computer's internal steps :
#
# 	Step no.	Prog. Line      Memory Updates/Condition Checks  
#   1               7          for a in 1, first takes 1
#   2               8           for b in range(1,3),takes 1
#   3               9           for c in range(1,3), takes 1
#   4               10          Prints, a as 1, b as 1, c as 1
#   5               9           for c in range takes 2
#   6               10          prints a as 1,b as 1 and c as 2
#   7               8           for b in range(1,3), takes 2
#   8               9           for c in range takes 1
#   9               10          prints a as 1, b as 2 c as 1
#   10              9           for c in range(1,3) takes c as 2
#   11              10          prints a as 1, b as 2 and c as 2
#   12              7           for a in [1,2], takes a as 2
#   13              8           for b in range(1,3) takes b as 1
#   14              9           for c in range(1,3). takes c as 1
#   15              10          prints a as 2, b as 1, c as 1
#   16              9           for c in range (1,3), takes c as 2
#   17              10          prints a as 2, b as 1 and c as 2
#   18              8           for b in range(1,3), takes b as 2
#   19              9           for c in range(1,3), takes c as 1
#   20              10          prints a as 2, b as 2, and c as 1
#   21              9           for c in range(1,2), takes c as 2
#   22              10          prints a as 2, b as 2, c as 2
