
# Find the last occurrence of a particular character

# Returns the index of the last occurrence of ch in str
#    If ch does not occur in str then return -1 (an invalid index, if seen from left to right)
def last_occurrence(str1,ch):
    n = len(str1)
    i = n-1
    ext = ""
    while(i != -1):
        if str1[i]==ch:
            return i
        i = i-1
    return -1
        


s = raw_input("Enter the string :")
c = raw_input("Enter the character :")
i = last_occurrence(s,c)

if(i==-1):
    print 'the character ',c,' is not in the string',s
else:
    print 'The last occurrence of ',s[i],' is at position ',i


#    Example sets
#
#    1) str = file.txt.pdf
#       ch = .  
#       Observable_Output : The last occurrence of . is at position 8 
#

#    2) str = aardvark.txt
#       ch = a  
#       Observable_Output : The last occurrence of a is at position 5
#
#    3) str = polynomial
#       ch = .
#       Observable_Output : The character . is not in the string "polynomial"
#


#     Trace format 
#
#    Example set 1
# 
#     Step    program_line    What_happens_inside_the_computer   
#        1        9              s = "file.txt.pdf"
#        2        10             c = '.'
#        3        11             last_occurrence(s,c) ==> last_occurrence('file.txt.pdf','.')
#
#     Step    program_line    Observable_Output
#        1
#

