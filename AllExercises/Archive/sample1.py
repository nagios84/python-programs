#Write a program that takes the value n and prints 1 to n

def ascending_counter(n):
    i = 1
    while(i<=n):
        print i
        i =i+1
    
n = int(raw_input("Enter a number :"))


ascending_counter(n)
