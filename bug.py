def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input types"

# Example usage with uncommon error
print(function_with_uncommon_error(10, 0))  # Output: Division by zero
print(function_with_uncommon_error(10, "a")) # Output: unsupported operand type(s) for /: 'int' and 'str'