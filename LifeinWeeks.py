#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#You have x days, y weeks, and z months left. 

age = input("What is your age? ")

yearsLeft = 90 - int(age)

daysLeft = yearsLeft*365
weeksLeft = yearsLeft*52
monthsLeft = yearsLeft*12

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left")

