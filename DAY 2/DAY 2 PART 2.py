import re

# Read the file.
inputfile = open("DAY 2\part1input.txt").readline()

splittedfile = inputfile.strip().split(",")

finalsplittedfile = []

total = 0

# CARDINAL SIN - REFERENCE REGEX METHOD HEAVILY.
# FOR FUTURE REFERENCE - USEFUL TO LEARN REGEX FORMULA.
regex = re.compile(r'^(..*?)\1{1,}$')

# For every line in the range list, we split it by the minus sign.

for item in splittedfile:

    currentrangesplitted = item.split("-")
    finalsplittedfile.append(currentrangesplitted)


for id in finalsplittedfile:

    for x in range(int(id[0]), int(id[1])):
        stringcompare = str(x)

        matchFlag = regex.search(stringcompare)

        if(matchFlag):
            print("PING")
            total += x

print(total)
        
