
#
#    Trace the following program
#

n=int(raw_input("Enter the value of n: "))#3
k=int(raw_input("Enter the value of k: "))#3

i=0			
while(i<n):		
    j=0		
    while(j<k):		
        print '*',
        j = j+1	
    print ""		
    i = i+1		

#
# What is the similarities between this and the program I gave in 2-exercises/4.py ?
# Answer - The only difference is instead of printing alphabets[i],this program will prints *

# 	Step no.	Prog. Line	Memory Updates/Condition Checks
#       1         	9           i = 0
#       2           10          checks while(i<3),while(0<3) == True
#       3           11          j = 0
#       4           12          checks while(j<3),while(0<3) == True
#       5           13          prints a '*'
#       6           14          j = j+1,j = 0+1 , J = 0
#       7           12          checks while(j<3),while(1<3) == True
#       8           13          prints a '*'
#       9           14          j = j+1, J = 1+1 = 2, J = 2
#       10          12          checks while(j<3),while(2<3) == True
#       11          13          prints a '*'
#       13          14          j = j+1, J = 2+1 = 3, J = 3
#       14          12          checks while(j<3),while(3<3) == False
#       15          15          Prints a empty line
#       16          16          i = i+1, i = 0+1 = 1,i = 1
#       17          10          checks while(i<3),while(1<3) == True    
#       18          11          j = 0
#       19          12          checks while(j<3),while(0<3) == True
#       20          13          prints a '*'
# Also write a program that does the following :
#
# Reads 2 integers n and k and prints the output as given below

integers= ['0', '1','2','3','4','5','6','7','8','9','10']
n=int(raw_input("Enter the value of n: "))#3
k=int(raw_input("Enter the value of k: "))#3
'''
i=0			
while(i<n):		
    j=0		
    while(j<k):		
        print integers[i],
        j = j+1	
    print ""		
    i = i+1		
#
# 0 0 0 0      0       (k times)  ---
# 1 1 1 1  ... 1                    |
# 2                                 |
# 3                                 |
# 4                                 |
# 5                                 |
# .                                 |
# .                                 |----- (n times)
# .                                 |
# .                                 |
# 9                                 |
# 0                                 |
# .                                 |
# .                                 |
#                                 ---
#
# Basically what I want you to do is write a program that prints n lines and each line prints a 
#     digit from 0,1,2 ... 9 one after another k times
#
#
#
#

'''
