import turtle
from turtle import*

"""
The font is a tuple containing:

    The font name such as ‘Arial’, ‘Courier’, or ‘Times New Roman’
    The font size in pixels
    The font type, which can be ‘normal’, ‘bold’, or ‘italic’

To set the alignment which controls how the text
is positioned based on the position of the turtle,
use the align parameter.
align can be set to one of these options: ‘left’, ‘center’, ‘right’
"""

turtle.color('Dark Red')
style = ('Arial', 30, 'bold')
turtle.write('Я жееееевиииийй! Я сееельниий!', font=style, align='center')
turtle.hideturtle()
done()