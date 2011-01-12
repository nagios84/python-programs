#
#	Trace the output. (nested ifs)
#	

		
n = int(raw_input("Enter a number"))				
if(n%2==0):								
	print n," is even"						
	if(n == 2):							
		print n," is 2, the smallest prime number"		
	else :							
		print n," is not prime since it	is dvisible by 2"	
else:									
	print n," is odd"					
	if(n%3==0 and n!=3):						
		print n," is not prime as it is divisible by 3"		
	else:								
		print n," is not divisible by 6"		
					

#
#     Trace the output.
#	
#
#	The format of the trace must be as follows (upto 20 steps is sufficient) :
# 	       Give some sample values for n and then trace the output,
#
#       Trace of the computer's internal steps :
#
# 	Step no.	Prog. Line      Memory Updates/Condition Checks  	
#	1		      5             n = 25	
#	2		      6		        (n%2 ==0) --> False
#	3		     12			    Does that else part
#   4            13             Prints n is odd
#   5            14             if(n%3==0 && n!=3): ---> false
#   6            16             Does the else part
#   7            17             prints 15 is not divisible by 6			

#   1           5               n = 33
#   2           6               (n%2 ==0) --> False
#   3           12              Does the else part
#   4           13          	Prints n is odd
#   5           14              if(n%3==0 && n!=3) --->True
#   6           15              Prints n is not a prime number as it is divisible by 3
