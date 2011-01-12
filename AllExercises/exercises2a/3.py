#
# Write a program that does the following :
#
# Reads an integer n  and prints the following
#
# 1                                                                       (1 time)
# 2    2                                                                  (2 times)
# 3    3    3                                                             (3 times)
# 4    4    4    4                                                        (4 times)
# .
# . 
# .
# .
# 11   11   11    11    11   11    11    11    11   11   11                (11 times)
# i    i    i     i                                               ..... i  (i times)
# .
# .
# . 
# .
# n
l = ['0','1','2','3','4','5','6','7','8','9','10']
n=int(raw_input("Enter the value of n: "))#3
k=int(raw_input("Enter the value of k: "))#3

i=0			
while(i<n):		
    j=0			
    while(j<i):		
        print l[i],
        j = j+1			
    print """"""""		
    i = i+1	
# 
# There must be a gap of exactly 4 spaces between any two digits on the same line
#
 
#
# Hint : Have a good look at 2.py of this same set and look for similarities.
#
