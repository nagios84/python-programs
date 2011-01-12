#Make a program where the user has to enter a secret password to use the program .You will know the password ofcourse (because it 'll help in your code).But your friend will either have to ask you, guess the password, or learn enough python to look at the code and figure out


password = "test123"
guess = raw_input ("Enter your password: ")

if guess ==password:
	print "Welcome, you are in"

else:
	print "WRONG PASSWORD TRY AGAIN"

