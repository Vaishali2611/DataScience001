class Calculator:
    def __init__(self):
        self.operations = {
            '1': self.add,
            '2': self.subtract,
            '3': self.multiply,
            '4': self.divide
        }

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

    def get_operation(self, choice):
        return self.operations.get(choice, None)

    def run(self):
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        while True:
            choice = input("Enter choice(1/2/3/4): ")
            operation = self.get_operation(choice)

            if operation:
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    continue

                result = operation(num1, num2)
                print(f"The result is: {result}")

                next_calculation = input("Do you want to perform another calculation? (yes/no): ")
                if next_calculation.lower() != 'yes':
                    break
            else:
                print("Invalid Input")

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
