num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

add = num1 + num2
mul = num1 * num2
sub = num1 - num2
div = num1 / num2 if num2 != 0 else "Undefined"

print(f"Addition: {add}")
print(f"Multiplication: {mul}")
print(f"Subtraction: {sub}")
print(f"Division: {div}")