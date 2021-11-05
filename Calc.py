def Calc():
    
    stack = []
    
    print("Please use the following notation: + for addition, - for subtraction, * for multiplication, and / for division. \n \n")
    print("Enter quit to end the application, clear to clear the number stack, and stack to see the currently saved numbers.")

    while True:
        try:
            
            expression = input()
            expressionAsList = expression.split()
            
            operations = {"+": lambda a,b: a+b, "-": lambda a,b: a-b, "*": lambda a,b: a*b, "/": lambda a,b: a/b}
            
            for token in expressionAsList:
                
                #User quit
                if token == 'quit':
                    quit()
                
                elif token == 'clear':
                    stack = []
                
                elif token == 'stack':
                    print(stack)

                #To handle non-numeric or non-operational inputs
                elif token not in operations:
                    try:
                        float(token)
                        stack.append(token)
                        #Appends token to stack if its a number

                    except ValueError:
                        print("Please enter a valid input.")

                elif token in operations:
                    n1 = float(stack.pop(-2))
                    n2 = float(stack.pop(-1))
                    sol = operations[token](n1, n2)
                    stack.append(sol)
                    print(str(n1) +" "+ token + " " + str(n2) + " = " + str(sol))

        except IndexError:
            print("No numbers have been entered, or stack does not contain two or more elements! Type 'stack' to see the current values saved!")
        
        except ZeroDivisionError:
            print("Cannot divide by zero")

Calc();
