import random
counter = 1
result = []
valuesYouCanHave = int(input("How many values can you get (e.g. w/ a coin, there are 2, w/ a dice, there are 6): "))
runTo = int(input("How many times do you want to run the test? "))
while counter <= runTo:
    result.append((random.randint(1,valuesYouCanHave)))
    counter += 1
print(result)