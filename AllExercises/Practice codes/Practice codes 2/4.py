# To swap two numbers

n1 = int(raw_input("Enter an Integer :"))
n2 = int(raw_input("Enter an integer :"))
temp = 0

print "The orginal values of (n1,n2) = ",(n1, n2)

temp = n1
n2 = n1
n1 = temp
n1 = n2

print "After swapping, values of (n1,n2)= (",n1,",",n2,")"

