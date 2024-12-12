from collections import Counter
from typing import List
import logging
import utils

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_list_difference(left_list: list[int], right_list: list[int]) -> int:
    '''
    Calculate the total absolute difference between corresponding values in two lists.

    Args:
        left_list (List[int]): The first list of integers.
        right_list (List[int]): The second list of integers.
    Returns:
        int: The sum of the absolute differences between corresponding elements.
    '''

    return sum(abs(left - right) for left, right in zip(utils.merge_sort(left_list), utils.merge_sort(right_list)))


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


def main():
    try:
        input_left: List[str]
        input_right: List[str]

        input_left, input_right = utils.read_input_from_file('input.txt')

        part_one_result: int = calculate_list_difference(
            input_left, input_right)
        logging.info('Part one result: %s', part_one_result)

        part_two_result: int = calculate_list_repetitions(
            input_left, input_right)
        logging.info('Part two result: %s', part_two_result)
    except Exception as e:
        logging.error('An error occurred: %s', e)


if __name__ == '__main__':
    main()
