
#  Calculator Package

#### Package helps to perform generic arithmetical operations as well resets memory and has operation to take (n)root.

*** 

## Main package consists from these operations: 

- add: Adds the provided number to the current result.
- subtract: Subtracts the provided number from the current result.
- multiply: Multiplies the current result by the provided number.
- divide: Divides the current result by the provided number.
- reset: Resets the current result to 0.
- n_root: Calculates the n-th root of the current result.

FYI - If an invalid operation is provided, the function returns the string "Invalid Operation".

***

## Overview of the methods:

- __init__(self): Initializes the Calculator object with a default value of 0.
- add(self, num): Adds num to the result and returns the updated result.
- subtract(self, num): Subtracts num from the result and returns the updated result.
- multiply(self, num): Multiplies the result by num and returns the updated result.
- divide(self, num): Divides the result by num and returns the updated result.
- n_root(self, n): Calculates the n-th root of the result and returns the result.
- reset(self): Resets the result to 0 and returns the new value of result.


***




## Installation

Create a virtual environment and install the package from TestPyPI:

```bash
 pip install -i https://test.pypi.org/simple/ calculator-Arturas-Kairaitis==0.0.2

```
once installed import the package:

```bash
from src.calculator_Arturas_Kairaitis import calculator
```

## Usage once Installed

```bash
Enter Operation (add, subtract, multiply, divide, reset, n_root, exit)
```

Note that it starts with zero and compounds depending on operation until 'reset' function used or 'exit' used and operations reset from 0 again.

***

### Limitations:

- The methods take only integer and floats.

- If you try to divide by zero (Calculator.divide(0)), outcome will be: 
 
 'Invalid Operation'
