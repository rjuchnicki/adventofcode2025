def part1(instructions: list[int]):
    count = 0
    pos = 50
    for i in instructions:
        pos = (pos + i) % 100

        if pos == 0:
            count += 1

    return count


if __name__ == "__main__":
    with open("data/day1.txt", "r") as f:
        instructions = [l.strip() for l in f.readlines()]

    instructions = [
        int(i[1:]) if i[0] == "R" else -int(i[1:]) for i in instructions
    ]

    print(part1(instructions))
