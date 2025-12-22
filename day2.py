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


def part2(id_ranges: list[list[int]]):
    total = 0
    for start, end in id_ranges:
        while start <= end:
            num_str = str(start)
            n = len(num_str)

            for i in range(1, n // 2 + 1):
                seq = num_str[:i]
                j = i

                made_with_repeated = True
                while j < n:
                    if num_str[j : j + i] != seq:
                        made_with_repeated = False
                        break
                    j += i

                if made_with_repeated:
                    total += start
                    break

            start += 1

    return total


if __name__ == "__main__":
    with open("data/day2.txt", "r") as f:
        id_ranges = [
            [int(i) for i in r.split("-")] for r in f.read().strip().split(",")
        ]

    print(part1(id_ranges))
    print(part2(id_ranges))
