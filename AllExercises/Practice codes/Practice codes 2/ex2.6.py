#Example of Nested While Loops

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
            
n = int(raw_input("Enter the value of n: "))
k = int(raw_input("Enter the value of k: "))

i = 0
while(i<n):
    j = 0
    while(j<k):
        print alphabets[i],
        j = j+1
    print ""
    i = i+1
    
    
#Not able to Understand
