#A soccer team is looking for girls from ages 10 to 12 to play on their team.Write a program to ask the users age and if male or female ("using "m" or "f").Display a message indicating whether the person is eligible to play on the team

sex = raw_input(" Are you male or female ? ('m or 'f')")
age = int (raw_input ("What is your age?"))

if sex == 'f' and age  >= 10 and age <=12:
	print " you can play on the team"
else:
	print "you do not have the  right age"

