num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

print(f"before swapping: num1={num1}, num2={num2}")

temp=num1
num1=num2
num2=temp

print(f"after swapping: num1={num1}, num2={num2}")