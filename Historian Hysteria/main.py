from collections import Counter
from typing import List, Tuple
from pathlib import Path

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_list_difference(left_list: List[int], right_list: List[int]) -> int:
    '''
    Calculate the total absolute difference between corresponding values in two lists.

    Args:
        left_list (List[int]): The first list of integers.
        right_list (List[int]): The second list of integers.
    Returns:
        int: The sum of the absolute differences between corresponding elements.
    '''

    return sum(abs(left - right) for left, right in zip(sorted(left_list), sorted(right_list)))


def calculate_list_repetitions(left_list: List[int], right_list: List[int]) -> int:
    '''
    Calculate the weighted sum of repetitions of values in `left_list` that appear in `right_list`.

    Args:
        left_list (List[int]): The list containing values to check.
        right_list (List[int]): The list in which to count occurrences of values from `left_list`.
    Returns:
        int: The total weighted sum of repetitions.
    '''

    return sum(value * Counter(right_list).get(value, 0) for value in left_list)


def read_input_from_file(file_name: str) -> Tuple[List[int], List[int]]:
    '''
    Reads the contents of a .txt file and returns it as a two lists of integers.

    Args:
        file_name (str): The name of the .txt file to be read.
    Returns:
        Tuple[List[int], List[int]]: Two lists of integers extracted from the file.
    '''
    try:
        file_path = Path(__file__).parent / file_name
        with file_path.open('r', encoding='utf-8') as file:
            left_list, right_list = [], []

            for line in file:
                if not line.strip() or len(line.strip().split()) != 2:
                    continue
                left, right = map(int, line.strip().split())
                left_list.append(left)
                right_list.append(right)
        return left_list, right_list
    except FileNotFoundError as e:
        logging.error('File not found: %s, Error: %s', file_name, e)


def main():
    try:
        input_left, input_right = read_input_from_file('input.txt')

        # Part one | Expected result: 1.320.851
        part_one_result = calculate_list_difference(input_left, input_right)
        logging.info('Part one result: %s', part_one_result)

        # Part two | Expected result: 26.859.182
        part_two_result = calculate_list_repetitions(input_left, input_right)
        logging.info('Part two result: %s', part_two_result)

    except Exception as e:
        logging.error('An error occurred: %s', e)


if __name__ == '__main__':
    main()
