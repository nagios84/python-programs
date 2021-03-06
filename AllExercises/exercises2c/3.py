#
# Find remaining string using first_occurrence(str,ch)
#

# copy the code you wrote in 2.py here
def first_occurrence(str1,ch):
    n = len(str1)
    i = 0
    while(i < n):
        if str1[i] == ch:
            return i
        i = i+1
    return -1
    
# Use the first_occurrence(str1,ch) to define string_after_firstOccurrence(str,ch)
#    If the character ch does not occur in str, then we return '' (the empty string)
#      else as in 1.py, we return the remaining string after ch.
def string_after_firstOccurrence(str2,ch):
    i = first_occurrence(str2,ch)+1
    n = len(str2)
    ext = ""
    while(i<n):
        ext = ext+str2[i]
        i = i+1
    return ext






'''print i
    ext = ""
    if(i== 0):
        return ''
    while True:
        try:
            ext += str2[i]
            i += 1
        except:
            break
         
    return ext '''
# Use the first_occurrence(str1,ch) to define string_after_firstOccurrence(str,ch)

s = raw_input("Enter the string")
c = raw_input("Enter the character")
str3=string_after_firstOccurrence(s,c)
print"The remaining string after the first occurrence of ",c," is ",str3


#     Trace format 
#
#    Example set 1
# 
#     Step    program_line    What_happens_inside_the_computer   
#        1        9              s = "file.txt.pdf"
#        2        10             c = '.'
#        3        11             calls string_after_firstOccurrence(s,c) ==> string_after_firstOccurrence('file.txt.pdf','.')
#       

#     Step    program_line    Observable_Output
#        1
#
#i = first_occurrence(str,ch)
#if(i==-1):
#return ''
#    Example sets
#
#    1) str = file.txt.pdf
#       ch = .  
#       Observable_Output : The remaining string after the first occurrence of . is txt.pdf
#

#    2) str = aardvark.txt
#       ch = a  
#       Observable_Output : The remaining string after the first occurrence of a is ardvark
#
#    3) str = polynomial-function
#       ch = o
#       Observable_Output : The remaining string after the first occurrence of o is lynomial-function
#


