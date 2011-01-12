#1) If the string does not contain ch it must return False
#2) Try doing things without the boolean record variable
#3) Split the program into well-defined functions with meaningful names
#and functionality.


# exactly_once(str,ch) returns true if the character ch occurs exactly once in str
#        otherwise return False
def exactly_once(str,ch):
	n = len(str)
	i = 0
	ext = ""
	record = False
	while(i<n):
		if record:
			ext=ext+str[i]
		if str[i]==ch:
			record = True
		i = i+1
	return False	
	print ext
	j = 0
	s = len(ext)
	while(j<s):
		if ext[j]== ch:
			return False
		j = j+1
	return True	
    					
#taaufiq   
'''j = 0
            while(j<s):
                if str[i]==ch:
                    print str[i]
                    j = j+1
                    return True
            return False
'''          
str=raw_input("Enter the string : ")
ch=raw_input("Enter the character : ")
print exactly_once(str,ch)

#
#    Example
#
#    Enter the string : ubuntu
#    Enter the character : b
#    True
#
#    Enter the string : apple
#    Enter the character : p
#    False
#
#    Enter the string : windows
#    Enter the character : w
#    False

