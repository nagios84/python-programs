#Example of a nested if:

n = int(raw_input("Enter a integer :"))

if (n%2 ==0):
    print n, "is even"
    if (n == 2):
        print n, "is the smallest prime number"
    else:
        print n, "is not prime since it divisible by 2"
        
else:
    print n,"is odd"
    if(n%3==0 and n!=3):
        print n, "is not prime as it is divisible by 3"
    else:
        print n, "is not divisible by 6"
    
