#
# Find the reverse of a given string
#

# Returns the reverse of a given string
#Using for:
def reverse1(str1):
    ext = ""
    for x in str1:
        print x
        ext = x+ext
    return ext

#Using While:
def reverse2(str1):
    ext = ""
    i = 0
    n = len(s)
    while(i<n):
        print str1[i]+ext
        ext= str1[i]+ext
        i = i+1
    return ext
    
#Using while, another method
def reverse3(str1):
    n = len(str1)
    i = n-1
    ext = ""
    while(i != -1):
        i = i-1
        #print str1[i]
        ext = ext+str1[i]
    return ext
    
#string = taufiq
#Sample program in the Interp
'''IndentationError: expected an indented block
>>> res = ""
>>> ext = ""
>>> str1 = "taufiq"
>>> for x in str1:
...     ext = x+ext
...     print ext
... 
t
at
uat
fuat
ifuat
qifuat
>>> x
'q'
'''
s = raw_input("Enter the string")
#rev=reverse1(s)
#rev=reverse2(s)
rev=reverse3(s)
print 'The reverse of the string \"",s," is \"',rev,'\"'


#    Example sets
#
#    1) str = pragmatic
#       Observable_Output : The reverse of the string "pragmatic" is "citamgarp"
#

#    2) str = citation
#       Observable_Output : The reverse of the string "citation" is "noitatic"


#     Trace format 
#
#    Example set 1
# 
#     Step    program_line    What_happens_inside_the_computer   
#        1        9              s = "file.txt.pdf"
#        2        10             c = '.'
#        3        11             calls remaining_string(s,c) ==> remaining_string('file.txt.pdf','.')
#
#     Step    program_line    Observable_Output
#        1
#

