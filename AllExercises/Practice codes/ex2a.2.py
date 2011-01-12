#Another Nested loop, but this time j<i

n = int(raw_input("Enter the value of n :"))
k = int(raw_input("Enter the value of k :"))

i = 0
while(i<n):
    j = 0
    while(j<i):
        print "*",
        j = j+1
    print ""
    i = i+1
    
#Able to Understand, Allhamdullilah
