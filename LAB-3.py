#Question no 1:
# List to store the numbers
numbers = []

# Loop through the range 1500 to 2700 (both inclusive)
for num in range(1500, 2701):
    # Check if the number is divisible by 7 and a multiple of 5
    if num % 7 == 0 and num % 5 == 0:
        numbers.append(num)

# Print the resulting numbers
print("Numbers divisible by 7 and multiple of 5 between 1500 and 2700 are:", numbers)

#question no 2:
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius_temp = float(input("Enter temperature in Celsius: "))
converted_fahrenheit = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp:.2f}°C is equivalent to {converted_fahrenheit:.2f}°F")

fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
converted_celsius = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp:.2f}°F is equivalent to {converted_celsius:.2f}°C")

#questuion no 3:
import random

# Generate a random number between 1 and 9
target_num = random.randint(1, 9)

while True:
     #Prompt the user to input a guess
    guess_num = int(input("Guess a number between 1 and 9: "))
    
    if guess_num == target_num:
        print("Well guessed!")
        break
    else:
        print("Incorrect! Try again.\n")
#question no 4:
#Function to print the pattern
def print_pattern(rows):
    # Print the upper half of the pattern
    for i in range(1, rows + 1):
        print('* ' * i)
    # Print the lower half of the pattern
    for i in range(rows - 1, 0, -1):
        print('* ' * i)

# Number of rows for the pattern
num_rows = 5
print_pattern(num_rows)

#Alternative of Pattern
print("\n")

def print_half_diamond(n):
    # Print the upper half of the diamond
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()
    
    # Print the lower half of the diamond
    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()


n = 5
print_half_diamond(n)

#Question no 5:
# Accept input from the user
user_string = input("Enter a string: ")

# Reverse  string
reversed_string = user_string[::-1]

# Print the reversed string
print("Reversed string:", reversed_string)

#question no 6:

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count, odd_count = 0, 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")

#question no 7:
items = [('class', 'V'), ('section', 'A'), True, 'resource', (0,-1), [5], {12}]

for item in items:
    print(f"{item} - {type(item)}")

#Question no 8:
for number in range(7):
    if number in [3, 6]:
        continue
    print(number, end=' ')

#Question no 9:
def fibonacci_fizzbuzz(n):
    a, b = 0, 1
    while a <= n:
        if a % 15 == 0:
            print("FizzBuzz")
        elif a % 3 == 0:
            print("Fizz")
        elif a % 5 == 0:
            print("Buzz")
        else:
            print(a)
        a, b = b, a + b

# Generate Fibonacci series up to 50
fibonacci_fizzbuzz(50)

#Question no 10:
def generate_2d_array(m, n):
    return [[i * j for j in range(n)] for i in range(m)]


rows = 3
columns = 3
array = generate_2d_array(rows, columns)
for row in array:
    print(row)

#Question no 11:
# Accepts multiple lines of input and prints them in lowercase
lines = []
print("Enter text (blank line to terminate):")
while True:
    line = input()
    if line:
        lines.append(line.lower())
    else:
        break
for line in lines:
    print(line)

#QUestion no 12:
# Accepts a sequence of binary numbers and prints those divisible by 5
binary_numbers = input("Enter binary numbers separated by a comma: ").split(',')
divisible_by_five = [num for num in binary_numbers if int(num, 2) % 5 == 0]
print(",".join(divisible_by_five))

#Question no 13:
# Accepts a string and calculates the number of letters and digits
s = input("Enter a string: ")
letters = digits = 0
for char in s:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
print(f"Letters {letters}\nDigits {digits}")

#question no 14:

import re

def validate_password(password):
    if (len(password) >= 6 and
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[$#@]", password)):
        return True
    else:
        return False

# Example usage:
password_to_test = input("Enter the password to validate: ")
if validate_password(password_to_test):
    print("Password is valid.")
else:
    print("Password is invalid.")