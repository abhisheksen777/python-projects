def display_menu():
    
    print("Calculator\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit\n")
    while True:
        try:
            choice=float(input("Enter choice :"))
            if 1<= choice <= 5:
                return choice
            else:
                print("Please enter a number between 1 and 5")
        except ValueError:
            print("Please enter a valid number.")
def get_numbers():
    while True:
        try:
            first=float(input("Enter first number :"))
            second=float(input("Enter second number :"))
            return first,second
        except ValueError:
            print("Please enter valid numbers.")
def calculate():
    while True:
        option=display_menu()
        if option == 5:
            print("Thanks for using the calc!")
            break
        num1,num2=get_numbers()
        if option == 1:
            result=num1+num2

        elif option == 2:
            result=num1-num2

        elif option == 3:
            result=num1*num2

        elif option == 4:
            if num2 == 0:
                print("Cannot divide by zero!")
                continue 
            result=num1/num2
            
        print(f"\nResult = {result}")
        answer = input("\nDo you want to continue? (yes/no): ").lower()
        if answer == "no":
            print("Goodbye!")
            break
calculate()
