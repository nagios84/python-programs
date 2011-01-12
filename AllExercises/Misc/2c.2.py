#Returns the index of the first occurence of ch in str

#if ch does not occur in str then return -1(as invalid index, if seen from left to right)

def first_occurence(str1, ch):
    n = len(str1)
    i = 0
    while(i < n):
        if str1[i] == ch:
            return i
        i = i+1
    return -1
       
s  = raw_input("Enter the string :")
c = raw_input("Enter the character :")

i = first_occurence (s,c)

if (i == -1):
    print "the character",c,"is not in the string,",s
else:
    print "the first position of ",s[i],"is at position",i
    


