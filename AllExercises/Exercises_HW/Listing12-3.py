#Modify the program from question #1 to display only the third name the user typed in

names = []
print "Enter 5 names"
for i in range(5):
	name = raw_input()
	names.append(name)

print "the third name is ",names[2] 
