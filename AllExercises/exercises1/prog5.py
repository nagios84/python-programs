# To swap two numbers with only two variables
#
# You may only add 2 lines in the program, after the three hashes

n1 = int(raw_input("Enter the number"))#1
n2 = int(raw_input("Enter the number"))#2

print "The original values of (n1,n2)= (",n1,",",n2,")"
#n1 = n1 + n2	# This is a hint for you ... Think !!!

n1 = n1+n2
n2=n1-n2
n1 = n1-n2

print "After swapping, values of (n1,n2)= (",n1,",",n2,")"




