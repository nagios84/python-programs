def stars(n):
	i = 1
	while(i<n):
		print '*',
		i = i+1
	print ""
	
	
def descending_stars(n):
	i = n
	while(i>0):
		stars(i)
		i = i-1
		
		
n = raw_input("Enter a number: ")

descending_stars(n)		
		
