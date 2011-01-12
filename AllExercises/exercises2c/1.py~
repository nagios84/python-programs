# Find the remaining string, (Please see the information given below the skeleton program)
def string_after_firstOccurrence(str,ch):
    n = len(str)
    i = 0
    record = False
    ext = ""
    while(i<n):
        if(record):       
            ext = ext + str[i]
        if str[i]== ch:
            record = True
        i = i+1
    return ext

s = raw_input("Enter the string :")#file.txt.pdf
c = raw_input("Enter the character :")#'.'

str1=string_after_firstOccurrence(s,c)
print "The remaining string after the first occurrence of ",c," is ",str1


#     Trace format 
#
#    Example set 1
# 
#     Step    program_line    What_happens_inside_the_computer   
#        1        9              s = "file.txt.pdf"
#        2        10             c = '.'
#        3        11             calls string_after_firstOccurrence(s,c) ==> remaining_string('file.txt.pdf','.
#        4        02             string_fater_first_occurence(file.txt.pdf,'.')
#        5        07             while(i<0),while(0<11) == True
#        6        08             if record, if false,code moves to line 10
#        7        10             if str[i] ==ch, if str[0] == '.', False,code moves to line 12                               
#        8        12             i = i+1 ,i= 0+1, i takes the value 2
#        9        13             code moves to to line number 7 and the loop continues until, str[4] ==ch
#       10        11             record = True
#       11        12             i = i+1, i = 4+1 = 5,
#       12        07             while(i<n), while(5<11)== True
#       13        08             if True
#       14        10             ext = ext+str[i], ext = ""+str[5], ext = t and the loop continues until i > n, then the loop breaks and comes out
#       15        13             returns ext
#


 

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

# Hint :
#    try the following in interpreter
#        >>> str = '' 
#        >>> str = str + 'a', 
#        >>> str
# (Basically str1+str2 returns the result of concatenating str1 and str2)


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

