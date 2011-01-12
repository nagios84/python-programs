#find(l,val) takes in a list of integers
#     and returns the first index of val in l if it exists 
#                 and returns -1 otherwise



def find(l,val):
        
    list = eval(l)    


l=raw_input("Enter a list")
x = raw_input("Enter a value to search for")

i = find(l,x)








if(i== -1):
    print val, "is not present in the list",list
else:
    print list[i],"is present in the list ",list,"at position",i
