import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

NumberOfLetters = int(input("How many letters would you like in your password?\n"))
NumberOfSymbols = int(input("How many symbols would you like?\n"))
NumberOfNumbers = int(input("How many numbers would you like?\n"))

## Eazy Level

# password = ""

# for char in range(1, NumberOfNumbers + 1):
#   password += random.choice(letters)

# for char in range(1, NumberOfSymbols + 1):
#   password += random.choice(symbols)

# for char in range(1, NumberOfNumbers + 1):
#   password += random.choice(numbers)

# print(password)

## Hard Level

passwordList = []

for char in range(1, NumberOfLetters + 1):
  passwordList.append(random.choice(letters))

for char in range(1, NumberOfSymbols + 1):
  passwordList += random.choice(symbols)

for char in range(1, NumberOfNumbers + 1):
  passwordList += random.choice(numbers)

random.shuffle(passwordList)

password = ""
for char in passwordList:
  password += char

print(f"Your password is: {password}")