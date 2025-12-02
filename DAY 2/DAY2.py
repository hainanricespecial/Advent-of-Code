import re

# Read the file.
inputfile = open("DAY 2\part1input.txt").readline()

splittedfile = inputfile.strip().split(",")

finalsplittedfile = []

total = 0

# For every line in the range list, we split it by the minus sign.

for item in splittedfile:

    currentrangesplitted = item.split("-")
    finalsplittedfile.append(currentrangesplitted)


for id in finalsplittedfile:

    for x in range(int(id[0]), int(id[1])):
        stringcompare = str(x)

        firsthalf = stringcompare[:len(stringcompare)//2]
        secondhalf = stringcompare[len(stringcompare)//2:]

        if(firsthalf == secondhalf):
            total += x

print(total)
        
