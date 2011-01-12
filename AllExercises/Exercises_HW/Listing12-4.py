#Modify the program from question#1 to let the user replace one of the names.She should be able to choose which name to replace, and then type in the new name.Finally,display the new list like this:


names = []
print "Enter 5 names"
for i in range(5):
	name = raw_input()
	names.append(name)

print names
print "Replace one name, Which one ?(1-5): "

