from pathlib import Path
from day_07_1 import read_equations, Equation


def evaluate_possible_equations(equations: list[Equation]) -> list[Equation]:
    possible_equations = []
    for equation in equations:
        result, numbers = equation
        if is_possible(numbers, result):
            possible_equations.append(equation)
    return possible_equations


def is_possible(numbers: list[int], expected_result: int) -> bool:
    possible_operators_combinations = get_all_possible_operators_combinations(len(numbers) - 1)
    for operator_combination in possible_operators_combinations:
        if calculate_result(numbers, operator_combination) == expected_result:
            return True
    return False


def calculate_result(numbers: list[int], operators: list[str]) -> int:
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i - 1] == "+":
            result += numbers[i]
        elif operators[i - 1] == "*":
            result *= numbers[i]
        else:
            result = int(f'{result}{numbers[i]}')
    return result


def get_all_possible_operators_combinations(size: int) -> list[list[str]]:
    if size == 1:
        return [["+"], ["*"], ["||"]]
    possible_combinations = []
    for combination in get_all_possible_operators_combinations(size - 1):
        possible_combinations.append(["+"] + combination)
        possible_combinations.append(["*"] + combination)
        possible_combinations.append(["||"] + combination)
    return possible_combinations


def main():
    equations = read_equations(Path("input.txt"))
    possible_equations = evaluate_possible_equations(equations)
    print(sum([equation[0] for equation in possible_equations]))


if __name__ == '__main__':
    main()
