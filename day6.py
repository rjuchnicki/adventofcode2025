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


if __name__ == "__main__":
    with open("data/day6.txt", "r") as f:
        input = f.readlines()

    operands = [[int(n) for n in i.split()] for i in input[:-1]]
    operators = input[-1].split()

    print(part1(operands, operators))
