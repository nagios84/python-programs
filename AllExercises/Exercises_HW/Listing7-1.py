#A store is having a sale.They are giving 10 Percent off purchases of $10 or lower, and 20 percent off purchases of greater than $10.Write a program that asks the purchase price and displays the discount (10% or 20%) and the final price

Purchase =  int (raw_input("How much did you purchase for :"))

if Purchase <= 10:
	discount = Purchase * 10

else:

	discount = Purchase * 20

final_price = Purchase - discount

print final_price 

