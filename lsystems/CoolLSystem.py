from LSystem import LSystem
from Symbol import Symbol

class CoolLSystem(LSystem):

    def __init__(self):
        super().__init__()
        self.rules['A'] = "+(90)T"
        self.rules['T'] = "[}F^>[+(60)[}F[+(60)T][-(60)T]]][-(60)[}F[+(60)T][-(60)T]]]]"
        self.axiom = Symbol('A', 0)