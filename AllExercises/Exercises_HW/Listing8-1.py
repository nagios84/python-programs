#Write a program to print a multiplication table (a times table).At the start , it should ask the user which table to print.

tables = int (raw_input("Which table to print: "))

for i in range(1,11):
	print  tables, 'x',i, '=',tables*i
