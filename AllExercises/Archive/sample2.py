#Write a program that takes the value n and prints n to 1

def descending_counter(n):
    i = n
    while(i !=-1 and i!=0):
        print i
        i =i-1
    
n = int(raw_input("Enter a number :"))

descending_counter(n)


