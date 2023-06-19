"""
I'm sure you're familiar with factorials – that is, the product of an integer and all the integers below it.

For example, 5! = 120, as 5 * 4 * 3 * 2 * 1 = 120

Your challenge is to create a function that takes any number and returns the number that it is a factorial of. So, if your function receives 120, it should return "5!" (as a string).

Of course, not every number is a factorial of another. In this case, your function would return "None" (as a string).
"""


def reverse_factorial(num: int):
    result = 1
    factorial = 1

    while result < num:
        factorial += 1
        result *= factorial
    if result == num:
        return str(factorial) + "!"
    else:
        return "None"
