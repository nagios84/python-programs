#Example1:

x = True
if x:
    y = 2
    if y:
        print('block2')
    print('block1')
print('block0')

#Example 2:

x = 'spam'
if 'rubbery' in 'shrubbery':
    print(x*8)
    x = x+'NI'
    print x
    if x.endswith('NI'):
        x = x*2
        print x 
