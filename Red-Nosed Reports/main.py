from typing import List
import logging
import utils

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def calculate_list_safety(input_list: List[List[int]]) -> int:
    '''
    Calculates the number of safe reports in a list of integer sequences.

    Args:
        input_list (List[List[int]]): A list of integer sequences (reports) to check.
    Returns:
        int: The count of safe reports.
    '''

    return sum(1 for values in input_list if utils.is_safe(values))


def calculate_list_safety_with_redundance(input_list: List[List[int]]) -> int:
    '''
    Determines the number of lists that are 'safe' or can be made 'safe' by removing one element.

    Args:
        input_list (List[List[int]]): A list of integer lists to evaluate.
    Returns:
        int: The count of lists that are "safe" or can be made "safe."
    '''

    safe_count: int = 0

    for values in input_list:
        if utils.is_safe(values):
            safe_count += 1
            continue

        for index in range(len(values)):
            modified_values = values[:index] + values[index + 1:]

            if utils.is_safe(modified_values):
                safe_count += 1
                break
    return safe_count


def main():
    try:
        input: List[list[int]] = utils.read_input_from_file('input.txt')

        part_one_result: int = calculate_list_safety(input)
        logging.info('Part one result: %s', part_one_result)

        part_two_result: int = calculate_list_safety_with_redundance(input)
        logging.info('Part two result: %s', part_two_result)
    except Exception as e:
        logging.error('An error occurred: %s', e, exc_info=True)


if __name__ == '__main__':
    main()
