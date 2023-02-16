class Calculator:
    """
    A simple calculator class that supports basic arithmetic operations and the ability to reset
    the current result and find the nth root of a number.
    """
    def __init__(self):
        """
        Initializes the calculator with a result of 0.
        """
        self.result = 0

    def add(self, num):
        """
        Adds the specified number to the current result.

        :param num: the number to add
        :return: the updated result
        """
        self.result += num
        return self.result

    def subtract(self, num):
        """
        Subtracts the specified number from the current result.

        :param num: the number to subtract
        :return: the updated result
        """
        self.result -= num
        return self.result

    def multiply(self, num):
        """
        Multiplies the current result by the specified number.

        :param num: the number to multiply by
        :return: the updated result
        """
        self.result *= num
        return self.result

    def divide(self, num):
        """
        Divides the current result by the specified number.

        :param num: the number to divide by
        :return: the updated result
        """
        self.result /= num
        return self.result

    def reset(self):
        """
        Resets the current result to 0.

        :return: the updated result
        """
        self.result = 0
        return self.result

    def n_root(self, n):
        """
        Finds the nth root of the current result.

        :param n: the root to find
        :return: the updated result
        """
        self.result = n ** (1 / n)
        return self.result


def perform_operation(calc, operation, num=None):
    """
    Performs the specified operation on the calculator with the given number, if applicable.

    :param calc: the calculator object to use
    :param operation: the operation to perform
    :param num: the number to use in the operation, if applicable
    :return: the result of the operation
    """
    if operation == "add":
        return calc.add(num)
    elif operation == "subtract":
        return calc.subtract(num)
    elif operation == "multiply":
        return calc.multiply(num)
    elif operation == "divide":
        return calc.divide(num)
    elif operation == "reset":
        return calc.reset()
    elif operation == "n_root":
        return calc.n_root(num)
    else:
        return "Invalid Operation"


calc = Calculator()

while True:
    print("Enter Operation (add, subtract, multiply, divide, reset, n_root, exit):")
    operation = input().lower()

    if operation == "exit":
        break
    elif operation in ["add", "subtract", "multiply", "divide", "reset"]:
        if operation in ["add", "subtract", "multiply", "divide"]:
            num = float(input("Enter number: "))
        else:
            num = None

        result = perform_operation(calc, operation, num)

    elif operation == "n_root":
        num = int(input("Enter root: "))
        result = perform_operation(calc, operation, num)

    else:
        result = perform_operation(calc, operation)

    print("Result:", result)
