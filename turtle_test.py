from turtle import mainloop
from lsystems.CoolLSystem import CoolLSystem
from Symbol import chain_to_string
from MyTurtle import MyTurtle, delay

lsystem = CoolLSystem()
my_turtle = MyTurtle()
delay(1)
chain = lsystem.generate_nth_chain(8)
print(str.format("drawing chain {}", chain_to_string(chain)))
my_turtle.process_chain(chain)
mainloop()

