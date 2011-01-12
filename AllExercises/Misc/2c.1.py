#
# Find the remaining string, (Please see the information given below the skeleton program)
#

# Hint :
#    try the following in interpreter
#        >>> str = '' 
#        >>> str = str + 'a', 
#        >>> str
# (Basically str1+str2 returns the result of concatenating str1 and str2)

def string_after_firstOccurrence(str,ch):
    n = len(str)
    i = 0
    while(i<n):
        if str[i] ==ch:
            for x in str[i+1]:
                i = i+1
            return x    



s = raw_input("Enter the string :")
c = raw_input("Enter the character :")
str1=string_after_firstOccurrence(s,c)
print "The remaining string after the first occurrence of ",c," is ",str1

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


#     Trace format 
#
#    Example set 1
# 
#     Step    program_line    What_happens_inside_the_computer   
#        1        9              s = "file.txt.pdf"
#        2        10             c = '.'
#        3        11             calls string_after_firstOccurrence(s,c) ==> remaining_string('file.txt.pdf','.')
#
#     Step    program_line    Observable_Output
#        1
#


# Note :- 
#    In all programs in this set, the following rules hold:
#    1) You can only add new code and not delete any line/character
#    2) You have to trace the code by hand on the example sets given below the program
#    3) The final trace must be available on the example inputs below the program
#
#    Besides the above rules, the spirit/manner in which you must develop the code is as follows, 
#        First you will have an idea then you code it up and then you run/trace the code on the example
#             sets and then you will realise the mistake(s) made. Then either you realise that the initial idea itself
#             was wrong and you change tracks, or, you refine the code and eliminate the bugs.           
#
#        Finally, I want to see the efforts taken by you in the trace below the final program.
#



 

