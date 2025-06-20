while (1):
    op = input("Enter operator or type 'exit' to quit: ")
     
    if op == "exit":
        print("Thank you for using!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
     
    
    if op == "+":
       print(num1 + num2)
    elif op == "-":
       print(num1 - num2)
    elif op == "/":
       print(num1 / num2)
    elif op == "*":
       print(num1 * num2)
    else:
       print("Invalid operator")  
        