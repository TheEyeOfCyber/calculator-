print("Calculator by The Eye Of Cyber")
print("\n")
print("          /|")
print("         / |")
print("        /  |")
print("       /   |")
print("      /    |")
print("     /     |")
print("    /______|")

#This will add the two numbers
def add(x, y):
    return x + y

#This will subtract the two numbers
def subtract(x, y):
    return x - y

#This will multiply the two numbers
def multiply(x, y):
    return x * y

#This will divide the two numbers
def divide(x, y):
    return x / y

print("\n")
print("Select Operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
         print("You are high on weed, please use correct number ")
    reuse = int(input("To use me again just enter any number and select option: "))
