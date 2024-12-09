from pathlib import Path
from typing import List


def calculate_list_safety(input_list: List[List[int]]) -> int:
    '''
    Calculates the number of safe reports in a list of integer sequences.

    Args:
        input_list (List[List[int]]): A list of integer sequences (reports) to check.
    Returns:
        int: The count of safe reports.
    '''

    def is_safe(values):
        increasing = all(values[i] < values[i + 1] for i in range(len(values) - 1))
        decreasing = all(values[i] > values[i + 1] for i in range(len(values) - 1))

        differences_valid = all(1 <= abs(values[i] - values[i + 1]) <= 3 for i in range(len(values) - 1))
        return (increasing or decreasing) and differences_valid

    safe_count = 0

    for values in input_list:
        if is_safe(values):
            safe_count += 1
    return safe_count


def calculate_list_safety_with_redundance(input_list: List[List[int]]) -> int:
    '''
    Determines the number of lists that are 'safe' or can be made 'safe' by removing one element.

    Args:
        input_list (List[List[int]]): A list of integer lists to evaluate.
    Returns:
        int: The count of lists that are "safe" or can be made "safe."
    '''

    def is_safe(values):
        increasing = all(values[i] < values[i + 1] for i in range(len(values) - 1))
        decreasing = all(values[i] > values[i + 1] for i in range(len(values) - 1))

        differences_valid = all(1 <= abs(values[i] - values[i + 1]) <= 3 for i in range(len(values) - 1))
        return (increasing or decreasing) and differences_valid

    safe_count = 0

    for values in input_list:
        if is_safe(values):
            safe_count += 1
        else:
            for index, _ in enumerate(values):
                values_temp = values.copy()
                values_temp.pop(index)

                if is_safe(values_temp):
                    safe_count += 1
                    break
                else:
                    continue

    return safe_count


def read_list_from_file(file_name: str) -> List[int]:
    file_path = Path(__file__).parent / file_name
    with file_path.open('r', encoding='utf-8') as file:
        return [[int(item) for item in line.split()] for line in file]


input = read_list_from_file('input.txt')

# Part one | Expected result: 379
response = calculate_list_safety(input)
print(f'Part one result: {response}')


# Part two | Expected result: 430
response = calculate_list_safety_with_redundance(input)
print(f'Part two result: {response}')
