#Display the string in the reverse order

str = str(raw_input("Enter a string : "))
n = len(str)

i = n-1
record = False

while(i<n and record ==  False):
    print str[i],
    if i == 0:
        record = True
    i = i-1
