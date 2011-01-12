#Modify the program from question#1 to print both the orginal list of names and a sorted list


names = []
print "Enter 5 names"
for i in range(5):
	name = raw_input()
	names.append(name)

print names
sorted_list = sorted(names)
print sorted_list
