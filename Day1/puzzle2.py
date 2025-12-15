# rawdata to string list
with open("puzzleInput", "r") as file:
    data = file.read().replace("\n", " ")
    dataElements = data.split(" ")

initValue = 50
cap = 100
password = 0
zeroPointer = 0

# assuming correct format
for step in dataElements:
    direction = step[0]
    value = int(step[1:])

    if direction == 'R':
        initValue += value
    else:
        initValue -= value

    while initValue >= cap:
        initValue -= cap
        password += 1

    while initValue < 0:
        initValue += cap
        if bool(zeroPointer):
            zeroPointer = 0
        else:
            password += 1

    if initValue == 0:
        zeroPointer = 1
        if direction == 'L':
            password += 1
    else:
        zeroPointer = 0

print(password)
