from collections import Counter
from typing import List, Tuple
from pathlib import Path


def calculate_list_difference(left_list: List[int], right_list: List[int]) -> int:
    '''
    Calculate the total absolute difference between corresponding values in two lists.

    Parameters:
        left_list (List[int]): The first list of integers.
        right_list (List[int]): The second list of integers.
    Returns:
        int: The sum of the absolute differences between corresponding elements.
    '''

    total_difference: int = sum(abs(left - right) for left, right in zip(sorted(left_list), sorted(right_list)))
    return total_difference


def calculate_list_repetitions(left_list: List[int], right_list: List[int]) -> int:
    '''
    Calculate the weighted sum of repetitions of values in `left_list` that appear in `right_list`.

    Parameters:
        left_list (List[int]): The list containing values to check.
        right_list (List[int]): The list in which to count occurrences of values from `left_list`.
    Returns:
        int: The total weighted sum of repetitions.
    '''

    total_repetitions: int = sum(value * Counter(right_list).get(value, 0) for value in left_list)
    return total_repetitions


def read_lists_from_file(file_name: str) -> Tuple[List[int], List[int]]:
    '''
    Read two lists of integers from a single input file.

    Parameters:
        file_name (str): The name of the input file containing paired integers in each line.
    Returns:
        Tuple[List[int], List[int]]: Two lists of integers extracted from the file.
    '''

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


input_left, input_right = read_lists_from_file('input.txt')

# Part one | Expected result: 1,320,851
response = calculate_list_difference(input_left, input_right)
print(f'Part one result: {response}')

# Part two | Expected result: 26,859,182
response = calculate_list_repetitions(input_left, input_right)
print(f'Part two result: {response}')
