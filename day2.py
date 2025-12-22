def part1(id_ranges: list[list[int]]):
    total = 0
    for start, end in id_ranges:
        while start <= end:
            num_str = str(start)
            n = len(num_str) // 2
            if num_str[:n] == num_str[n:]:
                total += start

            start += 1

    return total


if __name__ == "__main__":
    with open("data/day2.txt", "r") as f:
        id_ranges = [
            [int(i) for i in r.split("-")] for r in f.read().strip().split(",")
        ]

    print(part1(id_ranges))
