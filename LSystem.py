from Symbol import Symbol, string_to_chain, chain_to_string
class LSystem:
    rules = dict()
    axiom = Symbol('E', 0)

    def __init__(self):
        
        pass

    def generate_nth_chain(self, n: int):
        chain = [self.axiom]
        for i in range(n):
            ans = []
            for symbol in chain:
                ans = ans + self.get_derivation(symbol)
            chain = ans
        return chain

    def get_derivation(self, s: Symbol):
        if self.rules.__contains__(s.type):
            return string_to_chain(self.rules[s.type])
        else: 
            return [s]