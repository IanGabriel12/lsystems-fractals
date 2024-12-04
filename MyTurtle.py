from Symbol import Symbol
from turtle import *

class MyTurtle:
    interpretation = dict()
    LINE_LENGTH = 50

    def __init__(self):
        self.interpretation['f'] = self.move_forward_without_drawing
        self.interpretation['F'] = self.move_forward
        self.interpretation['+'] = self.turn_left
        self.interpretation['-'] = self.turn_right
        pass
    
    def process_chain(self, l):
        for symbol in l:
            self.execute_command(symbol)
    
    def execute_command(self, s: Symbol):
        return self.interpretation[s.type](s)
    
    def move_forward(self, s: Symbol):
        forward(self.LINE_LENGTH)
    
    def move_forward_without_drawing(self, s: Symbol):
        up()
        forward(self.LINE_LENGTH)
        down()
    
    def turn_left(self, s: Symbol):
        left(s.value)

    def turn_right(self, s: Symbol):
        right(s.value)

    