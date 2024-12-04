class Symbol:
    type: str
    value: int

    def __init__(self, type: str, value: int):
        self.type = type
        self.value = value
        pass

    def __str__(self):
        return str.format("{{ type: {0}, value: {1} }}", self.type, self.value)

'''
F -> Ir e desenhar para frente
f -> Ir para frente sem desenhar
+ -> Girar para esquerda
- -> Girar para direita
{ -> Aumentar comprimento do traço
} -> Diminuir comprimento do traço
> -> Aumentar cor
< -> Diminuir cor
[ -> Salvar estado do cursor na pilha
] -> Pop na pilha de estados e resetar o cursor para o estado que estava no topo
^ -> Aumentar grossura do traço
~ -> Diminuir grossura do traço
'''
TYPES = ['F', 'f', '+', '-', '{', '}', '>', '<', '[', ']', '^', '~']

def string_to_chain(s: str):
    '''
    Converts a string to a chain of symbols

    Args:
        s (str): the input string.
    
    Returns:
        List(Symbol): The alphabet chain this string represents.
    '''

    chain = []
    pos = 0
    while pos < len(s):
        if(s[pos] not in TYPES):
            raise SyntaxError("Invalid symbol: Not correct symbol type")
        
        if s[pos] == '+' or s[pos] == '-':
            symbol_type = s[pos]
            pos += 2
            t = ""
            while pos < len(s) and s[pos] != ')':
                t = t + s[pos]
                pos += 1
            
            if pos == len(s):
                raise SyntaxError('Invalid symbol: No closing parenthesis detected')
            
            deg_value = string_to_int(t)
            chain.append(Symbol(symbol_type, deg_value))
        else:
            chain.append(Symbol(s[pos], 0))
        pos += 1
    
    return chain

def string_to_int(t: str):
    try:
        val = int(t)
        return val
    except:
        raise SyntaxError('Degree change argument must be a number')

