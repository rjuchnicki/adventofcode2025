from collections import Counter


def part1(manifold: list[str]) -> int:
    splits = 0
    beams = [m if m == "." else "|" for m in manifold[0]]

    for row in manifold[1:]:
        new_beams = []

        i = 0
        while i < len(beams):
            if beams[i] == ".":
                new_beams.append(".")
                i += 1
                continue

            if row[i] == ".":
                new_beams.append("|")
                i += 1
            elif row[i] == "^":
                new_beams[i - 1] = "|"
                new_beams.append(".")
                new_beams.append("|")
                splits += 1
                i += 2

        beams = new_beams

    return splits


def part2(manifold: list[str]) -> int:
    beams = Counter({manifold[0].find("S"): 1})
    for m in manifold[2::2]:
        for i in range(len(m)):
            if m[i] == ".":
                continue

            beams[i - 1] += beams[i]
            beams[i + 1] += beams[i]
            beams[i] = 0

    return sum(beams.values())


if __name__ == "__main__":
    with open("data/day7.txt") as f:
        manifold = [l.strip() for l in f.readlines()]

    example = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]

    print(part1(example))
    print(part1(manifold))

    print(part2(example))
    print(part2(manifold))
