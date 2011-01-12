def first_occurence(str,ch):
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
        


def exactly_once(str,ch):
    i = first_occurence(str,ch)
    print i
    j = 0
	s = len(ext)
	while(j<s):
		if ext[j]== ch:
			return False
		j = j+1
	return True	
        
        
str=raw_input("Enter the string : ")
ch=raw_input("Enter the character : ")
print exactly_once(str,ch)        
        
