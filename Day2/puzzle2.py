import time

def invalid_id(fgroup, id):

    for factor in fgroup:
        skip = 0
        for i in range(factor):
            comp = id[i::factor]
            if comp != comp[0] * len(comp):
                skip = 1
                break
        if bool(skip):
            continue
        else:
            return True
    return False

# rawdata to string list
with open("puzzleInput", "r") as file:
    data = file.read()
    dataElements = data.split(",")

start_time = time.time()

invalidSum = 0

for current in dataElements:
    IDRange = current.split("-")
    currentID = IDRange[0]

    fgroup1 = []
    fgroup2 = []

    a = 1
    n0 = int(len(IDRange[0]))
    n1 = int(len(IDRange[1]))

    while a < 100:
        if n0 % a == 0:
            if a < n0:
                fgroup1.append(a)
        if n1 % a == 0:
            if a < n1:
                fgroup2.append(a)
        a += 1

    while int(currentID) <= int(IDRange[1]):

        if int(len(currentID)) == n0:
            if invalid_id(fgroup1, currentID):
                invalidSum += int(currentID)
        else:
            if invalid_id(fgroup2, currentID):
                invalidSum += int(currentID)
        currentID = str(int(currentID) + 1)

print(invalidSum)
print("--- %s seconds ---" % (time.time() - start_time))
