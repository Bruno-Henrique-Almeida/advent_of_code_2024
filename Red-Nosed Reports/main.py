from pathlib import Path
from typing import List

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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

    def is_safe(values: List):
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


def read_input_from_file(file_name: str) -> List[int]:
    '''
    Reads the contents of a .txt file and returns a list of integers.

    Args:
        file_name (str): The name of the .txt file to be read.
    Returns:
        str: The contents of the file.
    '''
    try:

        file_path = Path(__file__).parent / file_name
        with file_path.open('r', encoding='utf-8') as file:
            return [[int(item) for item in line.split()] for line in file]
    except FileNotFoundError as e:
        logging.error('File not found: %s, Error: %s', file_name, e)
        raise


def main():
    try:
        input: list = read_input_from_file('input.txt')

        # Part one | Expected result: 379
        part_one_result = calculate_list_safety(input)
        logging.info('Part one result: %s', part_one_result)


        # Part two | Expected result: 430
        part_two_result = calculate_list_safety_with_redundance(input)
        logging.info('Part two result: %s', part_two_result)

    except Exception as e:
        logging.error('An error occurred: %s', e)


if __name__ == '__main__':
    main()
