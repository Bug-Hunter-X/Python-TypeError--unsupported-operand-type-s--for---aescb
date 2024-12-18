def function_with_uncommon_error_solution(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid input types: Both inputs must be numbers"
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"

# Example usage
print(function_with_uncommon_error_solution(10, 0))  # Output: Division by zero
print(function_with_uncommon_error_solution(10, "a")) # Output: Invalid input types: Both inputs must be numbers
print(function_with_uncommon_error_solution(10, 2))   # Output: 5.0
print(function_with_uncommon_error_solution(10.5, 2))  # Output: 5.25