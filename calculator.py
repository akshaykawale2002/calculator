def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def display_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '5':
            print("Exiting the Calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("\nEnter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
