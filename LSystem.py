from Symbol import Symbol, string_to_chain, chain_to_string, is_empty

INITIAL_STATE = 0
INTERMEDIATE_STATE = 1
FINAL_STATE = 2
DEPTH_INDEX = 1
SYMBOL_INDEX = 0

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
    
    def __accepts_string(self, state: int, input_chain: list, stack: list, max_level: int):
        if state == INITIAL_STATE:
            return self.__accepts_string(INTERMEDIATE_STATE, input_chain, [(self.axiom, 0)], max_level)
        elif state == INTERMEDIATE_STATE:
            if is_empty(stack):
                return self.__accepts_string(FINAL_STATE, input_chain, stack, max_level)
            elif is_empty(input_chain):
                return False
            else:
                top_is_terminal_symbol = stack[-1][DEPTH_INDEX] == max_level
                next_symbol = input_chain[0]
                top_symbol = stack[-1][SYMBOL_INDEX]
                top_depth = stack[-1][DEPTH_INDEX]

                if top_is_terminal_symbol and next_symbol == top_symbol:
                    return self.__accepts_string(INTERMEDIATE_STATE, input_chain[1:], stack[:-1], max_level)
                elif top_is_terminal_symbol and not (next_symbol == top_symbol):
                    return False
                else:
                    derivation = self.get_derivation(stack[-1][0])
                    next_stack = stack[:-1]
                    for symbol in reversed(derivation):
                        next_stack.append((symbol, top_depth+1))
                    return self.__accepts_string(INTERMEDIATE_STATE, input_chain, next_stack, max_level)
        else:
            if is_empty(input_chain) and is_empty(stack):
                return True
            else:
                return False
            

    def accepts_string(self, input_str: str, max_level: int):
        return self.__accepts_string(INITIAL_STATE, string_to_chain(input_str), [], max_level);