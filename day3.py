def part1(banks: list[list[int]]) -> int:
    total = 0
    for bank in banks:
        max_i, max_first = max(enumerate(bank[:-1]), key=lambda x: x[1])
        max_second = max(bank[max_i + 1 :])
        total += 10 * max_first + max_second

    return total


def part2(banks: list[list[int]]) -> int:
    total = 0
    for bank in banks:
        joltage = 0
        start = 0

        for pow in range(11, -1, -1):
            end = len(bank) - pow
            max_i, max_digit = max(
                enumerate(bank[start:end]),
                key=lambda x: x[1],
            )
            joltage += max_digit * 10**pow
            start += max_i + 1

        total += joltage

    return total


if __name__ == "__main__":
    with open("data/day3.txt") as f:
        banks = [[int(c) for c in l.strip()] for l in f.readlines()]

    # example input
    # banks = [
    #     "987654321111111",
    #     "811111111111119",
    #     "234234234234278",
    #     "818181911112111",
    # ]
    # banks = [[int(c) for c in s] for s in banks]

    print(part1(banks))
    print(part2(banks))
