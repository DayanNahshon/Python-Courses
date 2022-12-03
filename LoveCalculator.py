print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

combinedNames = name1 + name2

t = combinedNames.count("t")
r = combinedNames.count("r")
u = combinedNames.count("u")
e = combinedNames.count("e")

firstDigit = t + r + u + e

l = combinedNames.count("l")
o = combinedNames.count("o")
v = combinedNames.count("v")
e = combinedNames.count("e")

secondDigit = l + o + v + e 

score = int(str(firstDigit) + str(secondDigit))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos")
elif (score >=40) and (score <= 50):
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
