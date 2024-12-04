from Symbol import Symbol
from CursorState import CursorState
from turtle import *

class MyTurtle:
    interpretation = dict()
    cursor_states = list()
    line_length = 50
    LINE_INCREASE_FACTOR = 0.1

    def __init__(self):
        self.interpretation['f'] = self.move_forward_without_drawing
        self.interpretation['F'] = self.move_forward
        self.interpretation['+'] = self.turn_left
        self.interpretation['-'] = self.turn_right

        self.interpretation['['] = self.save_cursor_state
        self.interpretation[']'] = self.restore_cursor_state
        self.interpretation['{'] = self.increase_line_length
        self.interpretation['}'] = self.decrease_line_length
        pass
    
    def process_chain(self, l):
        for symbol in l:
            self.execute_command(symbol)
    
    def execute_command(self, s: Symbol):
        if self.interpretation.__contains__(s.type):
            self.interpretation[s.type](s)
        return
    
    def move_forward(self, s: Symbol):
        forward(self.line_length)
    
    def move_forward_without_drawing(self, s: Symbol):
        up()
        forward(self.line_length)
        down()
    
    def turn_left(self, s: Symbol):
        left(s.value)

    def turn_right(self, s: Symbol):
        right(s.value)

    def save_cursor_state(self, s: Symbol):
        self.cursor_states.append(CursorState(
            x=xcor(), 
            y=ycor(), 
            angle=heading(),
            line_length=self.line_length
        ))
        pass
    
    def restore_cursor_state(self, s: Symbol):
        cursor_state: CursorState = self.cursor_states.pop()
        up()
        setx(cursor_state.x)
        sety(cursor_state.y)
        setheading(cursor_state.angle)
        self.line_length = cursor_state.line_length
        down()
        pass

    def increase_line_length(self, s: Symbol):
        self.line_length *= (1.0 + self.LINE_INCREASE_FACTOR)
        pass
    
    def decrease_line_length(self, s: Symbol):
        self.line_length *= (1.0 - self.LINE_INCREASE_FACTOR)
        pass

    