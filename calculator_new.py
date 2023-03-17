status = True
stop = False 

while status or stop:# if while loop is true running the program every time when be while loop is false stop the program
    
    while True: # if while loop is true running the program every time when be while loop is false stop the program
        
        try: # this is to fixed the error
            
            number_1 = float(input("Please enter the first number:==> ")) # get input numeric values from user
            break # this line to stop loop when be false
            
        except ValueError: #print type of error at windows uesr
            print("Please enter type of numeric value ") 
    while True:#if while loop is true running the program every time when be while loop is false stop the program
        try:
            operator = input("Plese enter type of opertor:==> ") # get input operator from user
            if operator in ["+", "-", "*", "/", "%", "//", "=", "<", ">", "^", "<=", ">=", "!="]:
             break
            else:
                raise ValueError
        except ValueError:
            print("the operator is wrong please enter type of operator (+,-*,/,%,//,=,<,>,^,<,=,>=,!=)")
    while True:#if while loop is true running the program every time when be while loop is false stop the program
        
        try: # this is to fixed the error
            
            number_2 = float(input("Please enter the second number:==> ")) # get input numeric values from user 
            if operator == "/" and number_2 == 0: # conditions satements when user enter division by zero 
                raise ZeroDivisionError
            break # this line to stop loop when be false 
        
        except ValueError: # print type of error 
            print("Please enter the type of numeric value ")
        except ZeroDivisionError:
            print("(this is zero division error)can not divised by zero, Please enter the another numeric value")
    
    if operator == "-": # conditionl satements number  substraction number
       print(number_1 - number_2)
         
    elif operator == "+": # conditionl satements number addition number
        print(number_1 + number_2)
        
    elif operator == "/":# conditionl satements number divsion number 
       print(number_1 / number_2)
       
    elif operator == "*":#conditionl satements number multiplication number 
        print(number_1 * number_2)
        
    elif operator == "%":# conditionl satements number modulus number 
       print(number_1 % number_2)
       
    elif operator == "//":# conditonl satements number floor division number 
       print(number_1 // number_2)
 
    elif operator == "^":# conditonl satements 	exponentiation  number
        print(number_1 ** number_2)
        
    elif operator == ">":# conditonl satements number greater than number
       print(number_1 > number_2)
       
    elif operator == "<":# conditionl satements number less than number 
        print(number_1 < number_2)
       
    elif operator == ">=":# conditionl satements number greater than  or equal to  number 
        print(number_1 >= number_2)
        
    elif operator == "<=":#conditionl satements number less than or equal to number 
       print(number_1 <= number_2)
       
    elif operator == "=":# conditionl satements number equal number 
        print(number_1 == number_2)
        
    elif operator == "!=":# conditionl satements number not equal number 
        print(number_1 != number_2)
    #else:
       # print("the operator is wrong please enter type of operator (+,*,/,=,%,-,>,< <=,>=,=,)")
    
    while status or stop:#if while loop is true running the program every time when be while loop is false stop the program
        try:
            repeat = str(input("do you want perform  another calculation (continue/stop)==> "))
            if repeat == "continue":
                status = True
                print("the program is continue")  
                break
            elif repeat == "stop":
                status = False
                print("the program is break") 
            else:
                raise ValueError   
        except ValueError:
            print("word incorrect if you want perform another calculation enter (continue) or do want to exit enter (stop)==> ") 
           
           
           
          
           
print("program exited")