while True:
    print("Choose an operation")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - divide")
    print("5 - Exit")
    option = int(input("Choose an operation:  "))
 

    if option == 5:
        print("Exiting the calculator mwa")
        break 

    if(option in [1,2,3,4]):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    
        if(option == 1):
            result = num1 + num2
        elif(option == 2):
            result = num1 - num2
        elif(option == 3):
            result = num1 * num2
        elif(option == 4):
            if num2 != 0:
                result = num1//num2
            else:
                print("Error! cannot be!")
                continue
            
        print("The result of the operation is {}".format(result))
        
    else:
         print("that is invalid")
    

        
        
     
          
        
            
        
        
