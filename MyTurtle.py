from Symbol import Symbol
from CursorState import CursorState
from turtle import *

class MyTurtle:
    interpretation = dict()
    cursor_states = list()
    line_length = 150
    line_thickness = 1

    LINE_THICKNESS_INCREMENT = 1
    LINE_INCREASE_FACTOR = 0.3

    colors = ["black", "red", "green", "blue", "yellow", "orange"]
    colors_pos = 0

    def __init__(self):
        self.interpretation['f'] = self.move_forward_without_drawing
        self.interpretation['F'] = self.move_forward
        self.interpretation['+'] = self.turn_left
        self.interpretation['-'] = self.turn_right

        self.interpretation['['] = self.save_cursor_state
        self.interpretation[']'] = self.restore_cursor_state
        self.interpretation['{'] = self.increase_line_length
        self.interpretation['}'] = self.decrease_line_length

        self.interpretation['>'] = self.set_next_color
        self.interpretation['<'] = self.set_previous_color

        self.interpretation['^'] = self.increase_line_thickness
        self.interpretation['~'] = self.decrease_line_thickness
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
            line_length=self.line_length,
            colors_pos=self.colors_pos,
            line_thickness=self.line_thickness
        ))
        pass
    
    def restore_cursor_state(self, s: Symbol):
        cursor_state: CursorState = self.cursor_states.pop()
        self.set_cursor_coordinates(cursor_state.x, cursor_state.y)
        self.set_cursor_heading(cursor_state.angle)
        self.set_line_length(cursor_state.line_length)
        self.set_cursor_color(cursor_state.colors_pos)
        self.set_line_thickness(cursor_state.line_thickness)
        pass
    
    def set_cursor_coordinates(self, x, y):
        up()
        setx(x)
        sety(y)
        down()
    def set_cursor_heading(self, angle):
        setheading(angle)
    def set_line_length(self, length):
        self.line_length = length
    def set_cursor_color(self, colors_pos):
        self.colors_pos = colors_pos
        color(self.colors[self.colors_pos])

    def increase_line_length(self, s: Symbol):
        self.line_length *= (1.0 + self.LINE_INCREASE_FACTOR)
        pass
    
    def decrease_line_length(self, s: Symbol):
        self.line_length *= (1.0 - self.LINE_INCREASE_FACTOR)
        pass

    def set_next_color(self, s: Symbol):
        self.set_cursor_color(self.colors_pos + 1)


    def set_previous_color(self, s: Symbol):
        self.set_cursor_color(self.colors_pos - 1)

    def increase_line_thickness(self, s: Symbol):
        self.set_line_thickness(self.line_thickness + self.LINE_THICKNESS_INCREMENT)
    
    def decrease_line_thickness(self, s: Symbol):
        self.set_line_thickness(self.line_thickness - self.LINE_THICKNESS_INCREMENT)
    
    def set_line_thickness(self, value):
        self.line_thickness = value;
        pensize(value)


    