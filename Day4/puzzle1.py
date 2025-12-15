def adjacent_paper(grid, index_i, index_j):
    adjacent_neighbours = 0
    paper_symbol = "@"
    rows = len(grid)
    cols = len(grid[0])

    top_con = 0
    bottom_con = 0
    i_inbounds = 0
    j_inbounds = 0

    # index i in bounds?
    if index_i <= rows - 1:
        i_inbounds = 1

    # index j in bounds?
    if index_j <= cols - 1:
        j_inbounds = 1

    # top
    if index_i > 0 and bool(j_inbounds):
        top_con = 1
        if grid[index_i - 1][index_j] == paper_symbol:
            adjacent_neighbours += 1

    # bottom
    if index_i < rows - 1 and bool(j_inbounds):
        bottom_con = 1
        if grid[index_i + 1][index_j] == paper_symbol:
            adjacent_neighbours += 1

    # left (include top-, bottom_left)
    if index_j > 0 and bool(i_inbounds):
        if grid[index_i][index_j - 1] == paper_symbol:
            adjacent_neighbours += 1
        if bool(top_con):
            if grid[index_i - 1][index_j - 1] == paper_symbol:
                adjacent_neighbours += 1
        if bool(bottom_con):
            if grid[index_i + 1][index_j - 1] == paper_symbol:
                adjacent_neighbours += 1

    # right (include top-, bottom_right)
    if index_j < cols - 1 and bool(i_inbounds):
        if grid[index_i][index_j + 1] == paper_symbol:
            adjacent_neighbours += 1
        if bool(top_con):
            if grid[index_i - 1][index_j + 1] == paper_symbol:
                adjacent_neighbours += 1
        if bool(bottom_con):
            if grid[index_i + 1][index_j + 1] == paper_symbol:
                adjacent_neighbours += 1

    if adjacent_neighbours < 4:
        return 1
    return 0


with open("puzzleInput", "r") as file:
    data = file.read().replace("\n", " ")
    this_grid = data.split(" ")
    this_rows = len(this_grid)
    this_cols = len(this_grid[0])

    result_papers = 0
    for this_i in range(this_rows):
        for this_j in range(this_cols):
            change = result_papers
            if this_grid[this_i][this_j] == "@":
                result_papers += adjacent_paper(this_grid, this_i, this_j)

    print(result_papers)

