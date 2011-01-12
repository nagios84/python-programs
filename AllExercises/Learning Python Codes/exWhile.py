#Example 1:
i = 0
y = 100
while True and y ==10:
    print 'x'
    i = i+0
else:
    print 'y'
#Example 2:
x = 'spam'
while x:
    print x,
    x =x[1:]

a = 0 ;b = 10
while a<b:
    print a
    a+= 1

#Example 3- Continue Loop

x = 10
while x:
    x = x-1
    if x%2 != 0:continue
    print x

    
#Example 4 :if print Nested under if(Without Continue)


x = 10
while x:
    x = x-1
    if x%2 == 0:
        print x
        
#Example 5 - break loop

while True:
    name=raw_input("Enter name :")
    if name == 'stop':break
    age = raw_input("Enter age")
    print ("hello",name,int(age) **2)
