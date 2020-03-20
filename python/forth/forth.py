import string

class StackUnderflowError(Exception):
    def __init__(self):
        self.message = 'Incorrect input values'
    
    def __str__(self):
        return repr(self.message)


class Stack:
    def stack_exists(func):
        def wrapper(self, *args):
            if not self.stack:
                raise StackUnderflowError()
            return func(self, *args)
        return wrapper
    
    def __init__(self):
        self.stack = []
    
    def add(self, data):
        self.stack.append(data)
    
    def do_math(self, x):
        res = ''
        res = self.pop() + res
        res = x + res
        res = self.pop() + res
        self.add(str(int(eval(res))))
    
    @stack_exists
    def pop(self):
        return self.stack.pop()
    
    @stack_exists
    def duplicate(self):
        self.add(self.stack[-1])
    
    @stack_exists
    def drop(self):
        self.stack = self.stack[:-1]
    
    @stack_exists    
    def swap(self):
        if  len(self.stack) == 1:
            raise StackUnderflowError()
        self.stack[-2], self.stack[-1] = self.stack[-1], self.stack[-2]
    
    @stack_exists
    def over(self):
        if  len(self.stack) == 1:
            raise StackUnderflowError()
        self.add(self.stack[-2])



def process_statement(x, st):
    if x.isdigit():
        st.add(x)
    elif x in '+*/-':
        st.do_math(x)
    elif x == 'dup':
        st.duplicate()
    elif x == 'drop':
        st.drop()
    elif x == 'swap':
        st.swap()
    elif x == 'over':
        st.over()
    return st



def evaluate(input_data):
    repl = {}
    for string in input_data:
        strng = string.lower().split(" ")
        if strng[0] == ':':
            word = strng[1]
            if word.isdigit():
                raise ValueError('Wrong input')
            rest = ' '.join(strng[2:-1])
            if word in rest:
                rest = rest.replace(word, repl[word])
            repl[word] = rest

            if rest in repl.values() and rest in repl:
                for key, value in repl.items():
                    if value == rest:
                        repl[key] = repl[rest]
            continue
            
        elif repl:
            if len(strng) == 1 and strng[0] in repl:
                strng0 = strng[0]
                strng[0] = repl[strng0]
            elif len(strng) > 1:
                for ind, s in enumerate(strng):
                    if s in repl:
                        strng[ind] = repl[s]

        elif strng[0].isalpha() and strng[0] not in ['dup', 'swap', 'over', 'drop']:
            raise ValueError('Wrong input')

        st = Stack()
        for s in ' '.join(strng).split():
            process_statement(s, st)
    return list(map(int, st.stack))
