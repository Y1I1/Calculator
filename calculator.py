
while True:
    while True:
        try:
            option = int(input('would you like to 1: use the calculator or 2: print out all previous equations '))
            break
        
        except ValueError:
            print('please enter a number try again: ')


    if option == 2:
        file = None

        try:
            file = open('input.txt', 'r')
            for line in file:
                print(line)
            file.close()

        except FileNotFoundError as error:
            print('the file that youre trying to open doesnt exist')
            print(error)

        finally:
            if file is not None:
                file.close()    
        break

    elif option == 1:    
        
        
        while True:
            try:
                num1 = int(input('enter a number: '))
                break
            
            except ValueError:
                print('please enter a number try again: ')

        while True:
            try:
                operation = (input('enter a +, -, * or /: '))
                if operation == '+' or operation == '-' or operation == '*' or operation =='/':
                    break
                else:
                    print('please enter +, *, /, -')    
            
            except ValueError:
                print('please enter a valid operation try again: ')

        while True:
            try:
                num2 = int(input('enter a number: '))
                break
            
            except ValueError:
                print('please enter a number try again: ')


        if operation == '+':
            ans = num1 + num2
            equation = f'{num1} + {num2} = {ans}'
            print(equation)

        elif operation == '-':
            ans = num1 - num2
            equation = f'{num1} - {num2} = {ans}'
            print(equation)

        elif operation == '*':
            ans = num1 * num2
            equation = f'{num1} * {num2} = {ans}'
            print(equation)

        elif operation == '/':
            ans = num1 / num2
            equation = f'{num1} / {num2} = {ans}'
            print(equation)

        file = None

        try:
            file = open('input.txt', 'a')
            file.write(f'{equation}\n')
            file.close()

        except FileNotFoundError as error:
            print('the file that youre trying to open doesnt exist')
            print(error)

        finally:
            if file is not None:
                file.close()
        
        break


    else:
        print('please enter 1 or 2')