from LSystem import LSystem
from Symbol import Symbol

class CoolLSystem(LSystem):

    def __init__(self):
        super().__init__()
        self.rules['T'] = "+(90)B"
        self.rules['B'] = "[}}}}F[+(60)B][FFL][-(60)B]]"
        self.rules['L'] = "[}}[+(60)F][F][-(60)F]]"
        self.axiom = Symbol('T', 0)