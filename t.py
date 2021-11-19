import random
import matplotlib.pyplot as plt
import numpy as np


def generateList(l, color, n):
    for i in range(n):
        l.append(color)


def generateChild(a, b):
    if a > b:
        c = b
        b = a
        a = c

    if a == 0:
        if b == 0:
            return random.choices(
                [0, 1, 2],
                weights=[0.75, 0.1875, 0.0625],
                k=2
            )
        elif b == 1:
            return random.choices(
                [0, 1, 2],
                weights=[0.50, 0.375, 0.125],
                k=2
            )

        elif b == 2:
            return random.choices(
                [0, 1, 2],
                weights=[0.50, 0.0, 0.50],
                k=2
            )
    elif a == 1:
        if b == 1:
            return random.choices(
                [0, 1, 2],
                weights=[0.01, 0.75, 0.25],
                k=2
            )
        elif b == 2:
            return random.choices(
                [0, 1, 2],
                weights=[0.0, 0.50, 0.50],
                k=2
            )
    else:
        return random.choices(
            [0, 1, 2],
            weights=[0.00, 0.01, 0.99],
            k=2
        )


people = []
numberOfBrownEyePeople = 0
numberOfGreenEyePeople = 30000
numberOfGreenBluePeople = 30000
generateList(people, 0, numberOfBrownEyePeople)
generateList(people, 1, numberOfGreenEyePeople)
generateList(people, 2, numberOfGreenBluePeople)


random.shuffle(people)
random.shuffle(people)
random.shuffle(people)
# print(people)

print("Generation::" + str(0) + "  Brown: " + str(people.count(0)) + "   Green: " +
      str(people.count(1)) + "   Blue: " + str(people.count(2)))


# print(generateChild(0, 0))

peopleCount = len(people)
# print("PeopleCount:" + str(peopleCount))


newGenerationList = []
brownHistory = []
greenHistory = []
blueHistory = []

brownHistory.append(people.count(0))
greenHistory.append(people.count(1))
blueHistory.append(people.count(2))

numberOfGenerations = 30

for y in range(numberOfGenerations):
    print("________________________________________________________")

    for x in range(int(peopleCount/2)):
        newGenPair = generateChild(people[x], people[x+1])
        newGenerationList = newGenerationList + newGenPair

    people = newGenerationList
    newGenerationList = []
    print("Generation::" + str(y) + "  Brown: " + str(people.count(0)) + "   Green: " +
          str(people.count(1)) + "   Blue: " + str(people.count(2)))
    brownHistory.append(people.count(0))
    greenHistory.append(people.count(1))
    blueHistory.append(people.count(2))


xA = np.array(list(range(0, numberOfGenerations+1)))
print(xA)
plt.plot(xA,  np.array(brownHistory), label="Brown eye", color="brown")
plt.plot(xA, np.array(greenHistory), label="Green eye", color="green")
plt.plot(xA, np.array(blueHistory), label="Blue eye", color="blue")

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
