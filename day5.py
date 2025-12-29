def part1(intervals: list[list[int]], ingredients: list[int]) -> int:
    num_fresh = 0
    for ingredient in ingredients:
        for interval in intervals:
            if ingredient >= interval[0] and ingredient <= interval[1]:
                num_fresh += 1
                break

    return num_fresh


def part2(intervals: list[list[int]]) -> int:
    sorted_intervals = sorted(intervals)
    merged = [sorted_intervals[0]]
    for interval in sorted_intervals[1:]:
        last = merged[-1]
        if interval[0] <= last[1]:
            merged[-1] = [last[0], max(last[1], interval[1])]
        else:
            merged.append(interval)

    total = 0
    for start, end in merged:
        total += end - start + 1

    return total


if __name__ == "__main__":
    with open("data/day5.txt") as f:
        input = f.read()
        intervals, ingredients = input.split("\n\n")

    intervals = [[int(n) for n in i.split("-")] for i in intervals.split("\n")]
    ingredients = [int(i) for i in ingredients.strip().split("\n")]

    print(part1(intervals, ingredients))
    print(part2(intervals))
