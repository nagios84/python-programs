#Get a file from the user and just display the extension

str = str(raw_input("Enter the name of the file with extension"))
n = len(str)
i = 0
record = False
ext = []
while(i<n):
    if str[i]=='.':
        record = True
    if record:        
        ext.append(str[i])
    i = i+1

l = eval('ext')
print l

#Did not understand the parts:
#1.print without lists
#2.Without flag
