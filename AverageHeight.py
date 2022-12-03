heights = input("Input a list of student heights: ").split()

for n in range(len(heights)):
    heights[n] = int(heights[n])

sumHeights = 0
for height in heights:
    sumHeights += height
print(f"Total height: {sumHeights}")

numberOfStudents = 0
for student in heights:
    numberOfStudents += 1
print(f"Number of students: {numberOfStudents}")

avgHeights = round(sumHeights/numberOfStudents)
print(avgHeights)
