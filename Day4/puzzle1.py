with open("testInput.txt", "f") as file:
    data = file.read().replace("\n", " ")
    dataElements = data.split(" ")

col_length = len(dataElements)
row_length = len(dataElements[0])

grid = [[0]* row_length] * col_length

for i in range(col_length):
    print("\n")
    for j in range(row_length):
        print(dataElements[j], end=" ")


# def adjacent_paper(grid, indexi, indexj):
