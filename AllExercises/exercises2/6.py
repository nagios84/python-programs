

alphabets = ['a','b','c','d','e','f','g','h','i','j','k',
             'l','m','n','o','p','q','r','s','t','u','v',
             'w','x','y','z']

n=int(raw_input("Enter the value of n: "))#5
k=int(raw_input("Enter the value of k: "))#3

i=0				
while(i<n):			
        j=0			
        while(j<k):				
            print alphabets[i],	
            j = j+1			
        print ""			
        i = i+1		
   
#
#     Trace the output.
#	
#
#	The format of the trace must be as follows (upto 20 steps is sufficient) :
#        Give some sample values for n and k 
#			and then trace the output and please note that you have to trace
#                       the exact output at each step as it would appear on the screen
#
#       Trace of the computer's internal steps :
#
# 	Step no.	Prog. Line	Memory Updates/Condition Checks  	
#       1           10      i =0
#       2           11      checks While(i<n),while(0<5) == True
#       3           12      j = 0
#       4           13      checks While(j<k),while(0<3) == True
#       5           14      print alphabets[i],alphabets[0] == a, prints a
#       6           15      j = j+1,j = 0+1 == 1, j = 1
#       7           13      cheks While(j<k),While(1<3) == True
#       8           14      print alphabets[i],alphabets[0] == a, prints a
#       9           15		j = j+1,j = 1+1 == 2, j = 2
#       10          13      cheks While(j<k),While(2<3) == True
#       11          14      print alphabets[i],alphabets[0] == a, prints a
#       12          15      j = j+1,j = 2+1 == 3, j = 3
#       13          16      Prints a empty line
#       14          17      i = i+1, i = 0+1 == 1, i = 1
#       15          11      checks while(i<n),checks while(1<5) == True
#       16          12      j = 0
#       17          13      checks while(j<k),checks while(0<3) == True
#       18          14      Print alphabets[i],alphabet[1] == b, prints b
#       19          15      j= j+1,j = 0+1 == 1, j = 1
#       20          13      cheks While(j<k),While(1<3) == True
#       21          14      print alphabets[i],alphabets[1] == b, prints b
#       22          15      j = j+1,j = 1+1 == 2, j = 2
#       23          13      cheks While(j<k),While(2<3) == True
#       24          14      print alphabets[i],alphabets[1] == b, prints b
#       25          15       j = j+1,j = 2+1 == 3, j = 3
#       26          13      prints an empy line
#       
#	 
#	 
#	  
#
#
#


