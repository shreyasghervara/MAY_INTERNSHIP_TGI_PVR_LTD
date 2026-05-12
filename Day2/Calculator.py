# calculator.py

def simple_calculator():
    print("=== Simple Calculator ===")

    try:
        first_number = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        second_number = float(input("Enter second number: "))

        if operator == "+":
            result = first_number + second_number

        elif operator == "-":
            result = first_number - second_number

        elif operator == "*":
            result = first_number * second_number

        elif operator == "/":
            if second_number == 0:
                print("Error: Cannot divide by zero.")
                return
            result = first_number / second_number

        else:
            print("Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")


simple_calculator()