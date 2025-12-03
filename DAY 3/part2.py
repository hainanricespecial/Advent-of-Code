# Read the file.
inputfile = open(r"DAY 3\input.txt")

total = 0

for line in inputfile:
    
# An attempt was made.
    maxfirstdigit = 0
    maxfirstindex = 0
    maxseconddigit = 0

    top12stash = []

    finaldigit = ''

    line.strip().replace('\n', '')

    length = len(line)

    for i in range(0, length - 1):

        # Shove into the stash.
        if(len(top12stash) < 12):
            top12stash.append(line[i])
        else:
            # Check if our
            if(int(line[i]) > int(min(top12stash))):
                minimumindex = top12stash.index(min(top12stash))
                top12stash.pop(minimumindex)
                top12stash.append(line[i])
    
    # Concat the strings based on the array.
    for entry in top12stash:
        finaldigit += entry

    total += int(finaldigit)


print("Your answer is: ", total)