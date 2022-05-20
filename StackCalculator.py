class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

prob = "6*(3-2)+3*4+2+1-4/2"

def step1(prob):
    pri = {'+':1, '-':1, '(':2, '*':0, '/':0}
    outstack = []
    #Operations should be stored in the stack.
    opstack = Stack()
    #Char could be 1)digit 2)brackets 3)operators
    for i in prob:
        if i.isdigit(): outstack.append(i)
        elif i == '(': opstack.push(i)
        elif i in '+-*/':
            if len(opstack) == 0: opstack.push(i)
            else:
                #Take out the higher priority operator, so it could be stacked higher,
                #so could be appended to the outstack earlier, which means
                #higher priority leads to higher priority in calculation.
                while (len(opstack) > 0) and (pri[opstack.top()] < pri[i]):
                    outstack.append(opstack.pop())
                opstack.push(i)
        elif i == ')':
            #Take out all the operators and append them to the outstack,
            #which means that operators in between brackets are calculated first.
            while opstack.top() != '(':
                outstack.append(opstack.pop())
            opstack.pop()
    #Append all the left operators to the outstack.
    while (len(opstack)>0):
        outstack.append(opstack.pop())
    return outstack

def step2(lst):
    numstack = Stack()
    for i in lst:
        if i.isdigit(): numstack.push(i)
        else:
            b, a = numstack.pop(), numstack.pop()
            c = str(eval(a+i+b))
            numstack.push(c)
    return numstack.pop()

print(step1(prob))
print(step2(step1(prob)))


