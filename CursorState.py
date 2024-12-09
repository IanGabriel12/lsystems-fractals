class CursorState:
    x = 0
    y = 0
    angle = 0
    line_length = 0
    colors_pos = 0
    line_thickness = 0
    def __init__(self, x=0, y=0, angle=0, line_length=0, colors_pos=0, line_thickness=0):
        self.x = x
        self.y = y
        self.angle = angle
        self.line_length = line_length
        self.colors_pos = colors_pos
        self.line_thickness = line_thickness
        pass