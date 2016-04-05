#Write a program that asks for your name, then house number, then street, then city, then province/territory/state ,then Postal/Zip Code(all in EasyGui dialog boxes).The Program should then display a mailing- style full address that looks something like this:

#John Snead
#28 Main Street
#Akron, Ohio
#12345
import easygui
name = easygui.enterbox("My name is: ", default = "Oscar")
Number = easygui.enterbox("My house Number is: ")
Street = easygui.enterbox("My street name is: ")
City = easygui.choicebox("My City name is :", choices = ["New York", "London", "Kabul"])
State = easygui.buttonbox("My State is: ", choices = ["USA", "UK", "Afganistan"])
Code = easygui.integerbox("My Postal code is: ")

address = name + " " + Number + "\n" + Street + " " + City + "\n" + State + " " + Code 

easygui.msgbox(address)


