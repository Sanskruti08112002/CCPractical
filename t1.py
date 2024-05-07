def find_largest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        return num1, num2, num3
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_user_input()
if __name__ == "__main__":
    print("Welcome to the largest number finder!")
    num1, num2, num3 = get_user_input()
    largest_number = find_largest_number(num1, num2, num3)
    print(f"The largest number is: {largest_number}")
