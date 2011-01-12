#
# Find the index of the first occurrence of a character
#

# Returns the index of the first occurrence of ch in str
#    If ch does not occur in str then return -1 (an invalid index, if seen from left to right)

def first_occurrence(str1,ch):
    n = len(str1)
    i = 0
    while(i < n):
        if str1[i] == ch:
            return i
        i = i+1
    return -1
s = raw_input("Enter the string :")
c = raw_input("Enter the character :")
i = first_occurrence(s,c)

if(i==-1):
    print 'the character ',c,' is not in the string ',s
else:
    print 'The first occurrence of ',s[i],' is at position ',i

#     Trace format 
#
#    Example set 1
# 
#     Step    program_line    What_happens_inside_the_computer   
#        1        9              s = "file.txt.pdf"
#        2        10             c = '.'
#        3        11             first_occurrence(s,c) ==> first_occurrence('file.txt.pdf','.')
#        4        08             first_occurrence('file.txt.pdf','.')
#        5        11             while(i<n),while(0<11) == True
#        6        12             if str[i] == ch, if str[0] = '.', False, code moves to line 14
#        7        14             i = i+1,i = 0+1 = 1, and the loop continues until str1[4] = '.', then returns i, if ch not in str,the loop comes out and
#                                 returns -1
#
#     Step    program_line    Observable_Output
#        1
#




#    Example sets
#
#    1) str = file.txt.pdf
#       ch = .  
#       Observable_Output : The first occurrence of . is at position 4 
#

#    2) str = aardvark.txt
#       ch = a  
#       Observable_Output : The first occurrence of a is at position 0 
#

#    3) str = polynomial
#       ch = .
#       Observable_Output : The character . is not in the string "polynomial"
#
