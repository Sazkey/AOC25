# rawdata to string list
with open("puzzleInput", "r") as file:
    data = file.read()
    dataElements = data.split(",")

invalidSum = 0

for current in dataElements:
    IDRange = current.split("-")
    currentID = IDRange[0]

    while int(currentID) <= int(IDRange[1]):
        if len(currentID) % 2 == 0:
            divisor = int(len(currentID) / 2)
            left = currentID[:divisor]
            right = currentID[divisor:]
            if int(left) == int(right):
                invalidSum += int(currentID)
        currentID = str(int(currentID) + 1)

print(invalidSum)
