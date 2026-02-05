while True:
    try:
        num1_input = input("Enter first number (or 'exit'): ")
        if num1_input.lower() == 'exit':
            break
        num1 = float(num1_input)

        operator = input("Enter operator (+, -, *, /): ").strip()
        if operator.lower() == 'exit':
            break
        
        num2_input = input("Enter second number (or 'exit'): ")
        if num2_input.lower() == 'exit':
            break
        num2 = float(num2_input)

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = num1 / num2
        else:
            print("Invalid operator.")
            continue
        
        print(f"Result: {result}\n")

    except ValueError:
        print("Invalid input. Please enter a number.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")

print("Goodbye!")
