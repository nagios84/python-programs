#Write a program that asks for your name, then house number, then street, then city, then province/territory/state ,then Postal/Zip Code(all in EasyGui dialog boxes).The Program should then display a mailing- style full address that looks something like this:

#John Snead
#28 Main Street
#Akron, Ohio
#12345
import easygui
name = easygui.enterbox("My name is :")
Number = easygui.enterbox("My house Number is :")
Street = easygui.enterbox("My street name is: ")
City = easygui.enterbox("My City name is :")
State = easygui.enterbox("My State is:")
Code = easygui.enterbox("My Postal code is:")

address = name + Number +  Street  + City + State  + Code 

easygui.msgbox(address)


