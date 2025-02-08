call_stack = []

def fibonacci(number):
    # Debugging: Storing function call stack
    call_stack.append(f'fibonacci{number}')
    
    # Base cases
    if number == 0:
        return 0
    if number == 1:
        return 1
    
    # Recursive calls
    return fibonacci(number - 1) + fibonacci(number - 2)

def execute():
    print(fibonacci(5))
    
    print("Recursive call sequence: ", call_stack)
    # Output: Recursive call sequence:  ['fibonacci5', 'fibonacci4', 'fibonacci3', 'fibonacci2', 'fibonacci1', 'fibonacci0', 'fibonacci1', 'fibonacci2', 'fibonacci1', 'fibonacci0', 'fibonacci3', 'fibonacci2', 'fibonacci1', 'fibonacci0', 'fibonacci1']

if __name__ == "__main__":
    execute()
    
# Function call sequence explanation:

# fibonacci(5) is called from execute
# fibonacci(5) calls -> fibonacci(4) and fibonacci(3)
# fibonacci(4) calls -> fibonacci(3) and fibonacci(2)
# fibonacci(3) calls -> fibonacci(2) and fibonacci(1)
# fibonacci(2) calls -> fibonacci(1) and fibonacci(0)

# Here, fibonacci(1) and fibonacci(0) return 1 and 0 respectively (base cases)
# So fibonacci(2) returns 1 + 0 = 1 to fibonacci(3)

# In fibonacci(3):
#           fibonacci(2) returned 1 
#           fibonacci(1) returns 1 (base case)
# Hence, fibonacci(3) returns 1 + 1 = 2 to fibonacci(4)

# In fibonacci(4):
#           fibonacci(3) returned 2
#           fibonacci(2) returns 1 (computed earlier)
# Hence, fibonacci(4) returns 2 + 1 = 3 to fibonacci(5)

# In fibonacci(5):
#           fibonacci(4) returned 3
#           fibonacci(3) returns 2 (computed earlier)
# Hence, fibonacci(5) returns 3 + 2 = 5 to execute

# Finally, the output "5" is printed when fibonacci(5) is called.
