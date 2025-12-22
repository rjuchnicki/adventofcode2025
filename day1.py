def part1(instructions: list[int]) -> int:
    count = 0
    pos = 50
    for i in instructions:
        pos = (pos + i) % 100
        if pos == 0:
            count += 1

    return count


def part2(instructions: list[int]) -> int:
    count = 0
    pos = 50
    for i in instructions:
        full_rotations, rem = divmod(abs(i), 100)
        count += full_rotations

        next_pos = pos + rem * (1 if i > 0 else -1)
        if pos != 0 and (i < 0 and next_pos <= 0) or (i > 0 and next_pos > 99):
            count += 1

        pos = next_pos % 100

    return count


if __name__ == "__main__":
    with open("data/day1.txt", "r") as f:
        instructions = [l.strip() for l in f.readlines()]

    instructions = [
        int(i[1:]) if i[0] == "R" else -int(i[1:]) for i in instructions
    ]

    print(part1(instructions))
    print(part2(instructions))
