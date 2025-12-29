import math


def part1(operands: list[list[int]], operators: list[str]):
    total = 0
    for i in range(len(operands[0])):
        inputs = [operand[i] for operand in operands]
        op = operators[i]
        if op == "+":
            total += sum(inputs)
        elif op == "*":
            total += math.prod(inputs)

    return total


def compute_result(numbers: list[str], operator: str) -> int:
    operands = [
        int("".join(n[i] for n in numbers)) for i in range(len(numbers[0]))
    ]
    return math.prod(operands) if operator == "*" else sum(operands)


def part2(operands_str: list[str], operators: list[str]):
    total = 0
    operator_index = len(operators) - 1
    numbers = [""] * len(operands_str)

    for i in range(len(operands_str[0]) - 1, -2, -1):
        # Final iteration: process remaining numbers
        if i == -1:
            total += compute_result(numbers, operators[operator_index])
            break

        # Space column indicates boundary between problems
        if all(s[i] == " " for s in operands_str):
            total += compute_result(numbers, operators[operator_index])
            numbers = [""] * len(operands_str)
            operator_index -= 1
            continue

        numbers = [
            operands_str[j][i] + numbers[j] for j in range(len(operands_str))
        ]

    return total


if __name__ == "__main__":
    with open("data/day6.txt") as f:
        input = f.readlines()

    operands = [[int(n) for n in i.split()] for i in input[:-1]]
    operands_str = [i.replace("\n", "") for i in input[:-1]]
    operators = input[-1].split()

    print(part1(operands, operators))
    print(part2(operands_str, operators))
