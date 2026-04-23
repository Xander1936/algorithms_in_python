# SImple Recursive Algorithms: Factorial Formula for n = 5

# Solution(1) with a function
def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact
print(iterative_factorial(5))  # Output: 120

# Solution(2) With recursion
# def recur_factorial(n):
#     if n == 1:
#         return n
#     else:
#         temp = recur_factorial(n-1) # The function calls itself with recur_factorial(n-1)
#         temp = temp * n
#     return temp

# print(recur_factorial(5))

# With 2 lines of code
def recur_factorial(n):
    if n == 1: return n
    else: return n * recur_factorial(n-1) # The function calls itself with recur_factorial(n-1)
    
print(recur_factorial(5))