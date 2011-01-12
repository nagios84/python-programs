'''Get a number from the user (n) and create an n x n box of "X"es on the screen. e.g. If they entered 12:
       XXXXXXXXXXXX
       XXXXXXXXXXXX
       XXXXXXXXXXXX '''
       
n = int(raw_input("Enter a value for n :"))
k = int(raw_input("Enter a value for k : "))       
i=0			
while(i<n):		
    j=0			
    while(j<k):		
        print 'X',
        j = j+1			
    print """"""""		
    i = i+1	
    
#Able to understand, Allhamdullilah
