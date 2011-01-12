
# Using last occurrence and other functions created in this set,
#        return the remaining string after the last occurrence of the character.

# copy the code you wrote in 5.py here
def last_occurrence(str1,ch):
    n = len(str1)
    i = n-1
    ext = ""
    while(i != -1):
        if str1[i]==ch:
            return i
        i = i-1
    return -1  

# Use the first_occurrence(str,ch) to define string_after_firstOccurrence(str,ch)
#    If the character ch does not occur in str, then we return '' (the empty string)
#      else as in 1.py, we return the remaining string after ch.
def string_after_lastOccurrence(str2,ch):
    i = last_occurrence(str2,ch)
    if(i==-1):
        return ''
    n = len(str2)
    ext = ""
    while(i<n):
        ext = ext+str2[i]
        i = i+1
    return ext





s = raw_input("Enter the string :")
c = raw_input("Enter the character :")
str1=string_after_lastOccurrence(s,c)
print"The remaining string after the last occurrence of ",c," is \"",str1,"\""

#    Example sets
#
#    1) str = file.txt.pdf
#       ch = .  
#       Observable_Output : The remaining string after the last occurrence of . is "pdf"
#

#    2) str = aardvark.txt
#       ch = a  
#       Observable_Output : The remaining string after the first occurrence of a is "rk.txt"
#
#    3) str = polynomial-function
#       ch = n
#       Observable_Output : The remaining string after the last occurrence of n is ""
#


#     Trace format 
#
#    Example set 1
# 
#     Step    program_line    What_happens_inside_the_computer   
#        1        9              s = "file.txt.pdf"
#        2        10             c = '.'
#        3        11             calls string_after_firstOccurrence(s,c) ==> string_after_firstOccurrence('file.txt.pdf','.')x
#
#     Step    program_line    Observable_Output
#        1
#



