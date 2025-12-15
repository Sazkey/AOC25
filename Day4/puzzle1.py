with open("testInput.txt", "f") as file:
    data = file.read().replace("\n", " ")
    dataElements = data.split(" ")

rows = len(dataElements)
cols = len(dataElements[0])

# def adjacent_paper(grid, indexi, indexj):
