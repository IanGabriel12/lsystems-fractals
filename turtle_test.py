from turtle import mainloop
from Symbol import string_to_chain
from MyTurtle import MyTurtle

chain = string_to_chain("F+(90)F-(90)F-(90)FF")
my_turtle = MyTurtle()
my_turtle.process_chain(chain)
mainloop()