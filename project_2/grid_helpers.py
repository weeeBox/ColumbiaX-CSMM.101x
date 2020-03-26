from Grid import Grid


def clone_grid(grid: Grid) -> Grid:
    size = grid.size
    copy = Grid(size)
    for i in range(size):
        for j in range(size):
            copy.map[i][j] = grid.map[i][j]
    return copy
