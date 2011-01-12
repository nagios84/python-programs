#Try changing the temperature conversion program from chapter 5 to use GUI input and output instead of raw_input() and print

import easygui
easygui.msgbox('This program converts Fahrenheit to Celsius')
temp = easygui.enterbox("Temp in Fahrenheit")
F= float(temp)
Cel = (F- 32)*5.0/9
easygui.msgbox(Cel), "Celsius"

