# Read the file.
inputfile = open(r"DAY 3\input.txt")

total = 0

for line in inputfile:

    maxfirstdigit = 0
    maxfirstindex = 0

    maxseconddigit = 0


    line.strip().replace('\n', '')

    length = len(line)

    for i in range(0, length - 2):

        if(int(maxfirstdigit) < int(line[i])):
            maxfirstdigit = line[i]
            maxfirstindex = i

    for j in range(maxfirstindex + 1, length - 1):
        if(int(maxseconddigit) < int(line[j])):
            maxseconddigit = line[j]

    # Concat the numbers.        
    finaldigit = maxfirstdigit + maxseconddigit

    total += int(finaldigit)

print("Your answer is: ", total)


        

