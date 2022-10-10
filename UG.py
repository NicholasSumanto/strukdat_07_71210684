class PrefixConverter: 
    def __init__(self): 
        self.stackList = ['?']

    def push(self,data): 
        self.stackList.append(data)

    def peek(self): 
        if self.stackList: 
            return self.stackList[-1] 
        else: 
            return "Isi Stack Kosong"
    
    def pop(self): 
        if self.stackList: 
            data = self.stackList.pop(-1) 
            return data 
        else: 
            return "Isi Stack Kosong"

    def cekValidExpression(self,expression):
        for i in range (len(expression)):
            if i == "(":
                return "Expresi Infix yang anda masukkan tidak valid!!"
            

    def infixToPrefix(self,expression):
        operators = []
        operands = []
 
        for i in range(len(expression)):
            
            if (expression[i] == '(' ):
                operators.append(expression[i])
    
            elif (expression[i] == ')'):
                while (len(operators)!=0 and (operators[-1] != '(' )):
                    op1 = operands[-1]
                    operands.pop()
                    op2 = operands[-1]
                    operands.pop()
                    op = operators[-1]
                    operators.pop()
                    tmp = op + op2 + op1
                    operands.append(tmp)
                operators.pop()
            elif (not self.cekValidExpression(expression[i])):
                operands.append(expression[i] + "")
    
            else:
                while (len(operators)!=0 and self.cekValidExpression(expression[i]) <= self.cekValidExpression(operators[-1])):
                    op1 = operands[-1]
                    operands.pop()
    
                    op2 = operands[-1]
                    operands.pop()
    
                    op = operators[-1]
                    operators.pop()
    
                    tmp = op + op2 + op1
                    operands.append(tmp)
                operators.append(expression[i])
    
        while (len(operators)!=0):
            op1 = operands[-1]
            operands.pop()
    
            op2 = operands[-1]
            operands.pop()
    
            op = operators[-1]
            operators.pop()
    
            tmp = op + op2 + op1
            operands.append(tmp)
        return operands[-1]

if __name__ == '__main__': 
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1")) 
    print(expresi1.infixToPrefix("A * (B + C) / D")) 
    print(expresi1.infixToPrefix("(1+2)*3")) 
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289")) 
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))
        
        
