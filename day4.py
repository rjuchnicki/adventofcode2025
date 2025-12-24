DIRS: list[tuple[int, int]] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def is_accessible(grid: list[list[str]], i: int, j: int) -> bool:
    adjacent = 0
    for di, dj in DIRS:
        new_i = i + di
        new_j = j + dj
        if (
            0 <= new_i < len(grid)
            and 0 <= new_j < len(grid[0])
            and grid[new_i][new_j] == "@"
        ):
            adjacent += 1

    if adjacent < 4:
        return True

    return False


def part1(grid: list[list[str]]) -> int:
    accessible = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ".":
                continue

            if is_accessible(grid, i, j):
                accessible += 1

    return accessible


def part2(grid: list[list[str]]) -> int:
    removed = 0
    while True:
        removed_this_pass = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == ".":
                    continue

                if is_accessible(grid, i, j):
                    removed_this_pass += 1
                    grid[i][j] = "."

        if removed_this_pass == 0:
            break
        removed += removed_this_pass

    return removed


if __name__ == "__main__":
    with open("data/day4.txt", "r") as f:
        grid = [[c for c in l.strip()] for l in f.readlines()]

    print(part1(grid))
    print(part2(grid))
