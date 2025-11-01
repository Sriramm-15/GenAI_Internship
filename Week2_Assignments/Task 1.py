#task 1:Python Basics&Operators

#1.1: Create a Python script that accepts two numbers from the user
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))

#1.2:Perform all basic arithmetic operations (add, subtract, multiply, divide, modulus, power)
add=n1+n2
sub=n1-n2
mul=n1*n2
div=n1/n2
mod=n1%n2
power=n1**n2
print("Addition:",add)
print("Subtraction:",sub)
print("Multiplication:",mul)
print("Division:",div)
print("Modulus:",mod)
print("Power:",power)

#1.3:Demonstrate use of comparison and logical operators (>, <, ==, !=, and, or, not).
print("\n Comparison Operators")
print("n1 is greater than n2:", n1 > n2)
print("n1 is less than n2:", n1 < n2)
print("Borth are equal:", n1 == n2)
print("Not equal :", n1 != n2)

print("\n Logical Operators")

if (n1 > 0) and (n2 > 0):
    print("Both numbers are positive.")
else:
    print("At least one number is not positive.")

if (n1 > 0) or (n2 > 0):
    print("At least one number is positive.")
else:
    print("Both numbers are non-positive.")

if not (n1 > n2):
    print("n1 is not greater than n2.")
else:
    print("n1 is greater than n2.")


# 1.4:Print results clearly using formatted output (f-strings)
print("\n Formatted Summary (Using f-strings)")
print(f"Numbers entered: {n1} and {n2}")
print(f"Sum: {add}")
print(f"Difference: {sub}")
print(f"Product: {mul}")
print(f"Division: {div:.2f}")
print(f"Modulus: {mod}")
print(f"Power: {power}")
print(f"Is {n1} greater than {n2}? {'Yes' if n1 > n2 else 'No'}")
