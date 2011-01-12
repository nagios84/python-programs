#Redo this program using while loop.

#n = int(raw_input("Enter an integer"))
#l = range(1,n)
#1

#for i in l:
#    print i
    
    
#Same Program with While loop
l = [1.2]
i = 0
while(i<l):
    j = 0
    while(j<l):
        print i
        j = j+1
    print ""
    i =i+1
       
       
       
#Did not understand       
       
       
      
'''#
#	Trace the output. (nested function calls)
#	
#

def starts_with(str,c):		
	if(str[0] == c):	
		return True			
	return False			
				
def second_letter(str,c):		
	if(str[1]=='b'):		
		return True			
	return False			
			
def starts_with_ab(str):			
	if(not(starts_with(str,'a'))):			
		return False				
	if(not(second_letter(str,'b'))):		
		return False				
	return True					
	
	
str1 = raw_input("Enter a string of a's and b's : ")
if(starts_with_ab(str1)):				
	print str1," starts with ab
'''
