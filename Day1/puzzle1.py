# rawdata to string list
with open("puzzleInput", "r") as file:
    data = file.read().replace("\n", " ")
    dataElements = data.split(" ")

initValue = 50
cap = 100
password = 0

# assuming correct format
for step in dataElements:
    direction = step[0]
    value = int(step[1:])

    while value >= cap:
        value -= cap

    if direction == 'R':
        initValue += value
    else:
        initValue -= value

    while initValue >= cap:
        initValue -= cap

    while initValue < 0:
        initValue += cap

    if initValue == 0:
        password += 1

print(password)
