from typing import List
import utils

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
        increasing: bool = all(values[i] < values[i + 1] for i in range(len(values) - 1))
        decreasing: bool = all(values[i] > values[i + 1] for i in range(len(values) - 1))

        differences_valid: bool = all(1 <= abs(values[i] - values[i + 1]) <= 3 for i in range(len(values) - 1))
        return (increasing or decreasing) and differences_valid

    safe_count: int = 0

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
        increasing: bool = all(values[i] < values[i + 1] for i in range(len(values) - 1))
        decreasing: bool = all(values[i] > values[i + 1] for i in range(len(values) - 1))

        differences_valid: bool = all(1 <= abs(values[i] - values[i + 1]) <= 3 for i in range(len(values) - 1))
        return (increasing or decreasing) and differences_valid

    safe_count: int = 0

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


def main():
    try:
        input: List[int] = utils.read_input_from_file('input.txt')

        part_one_result: int = calculate_list_safety(input)
        logging.info('Part one result: %s', part_one_result)

        part_two_result: int = calculate_list_safety_with_redundance(input)
        logging.info('Part two result: %s', part_two_result)
    except Exception as e:
        logging.error('An error occurred: %s', e)


if __name__ == '__main__':
    main()
