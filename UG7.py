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
            if i == "(" :
                return "Expresi Infix yang anda masukkan tidak valid!!"
            else :
                return  1

    def infixToPrefix(self,expression):
        operands = []
 
        for i in range(len(expression)):
            
            if (expression[i] == '(' ):
                self.append(expression[i])
    
            elif (expression[i] == ')'):
                while (len(self)!=0 and (self[-1] != '(' )):
                    op1 = operands[-1]
                    self.pop()
                    op2 = operands[-1]
                    self.pop()
                    op = self[-1]
                    self.pop()
                    tmp = op + op2 + op1
                    operands.append(tmp)
                self.pop()
            elif (not self.cekValidExpression(expression[i])):
                operands.append(expression[i] + "")
    
            else:
                while (len(self)!=0 and self.cekValidExpression(expression[i]) <= self.cekValidExpression(self[-1])):
                    op1 = operands[-1]
                    operands.pop()
    
                    op2 = operands[-1]
                    operands.pop()
    
                    op = self[-1]
                    self.pop()
    
                    tmp = op + op2 + op1
                    operands.append(tmp)
                self.append(expression[i])
    
        while (len(self)!=0):
            op1 = operands[-1]
            operands.pop()
    
            op2 = operands[-1]
            operands.pop()
    
            op = self[-1]
            self.pop()
    
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
        
        
