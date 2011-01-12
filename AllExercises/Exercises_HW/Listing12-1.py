#Write a program to ask the user for five names.The program should store the names in list, and print them all out at the end.It should look something like this:

#Enter 5 names:
#Tony
#Paul
#Nick
#Michel
#Kevin
#The names are Tony Paul Nick Michel Kevin

names = []
print "Enter 5 names"
for i in range(5):
	name = raw_input()
	names.append(name)

print names
