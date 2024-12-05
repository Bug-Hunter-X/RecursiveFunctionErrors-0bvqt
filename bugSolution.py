def factorial(n):
    if n < 0:
        return None # Or raise an exception: raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(-1)) # This will now return None or raise an exception