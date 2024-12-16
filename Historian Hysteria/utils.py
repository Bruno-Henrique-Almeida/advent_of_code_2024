from typing import List, Tuple
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def merge_sort(input_list: List[int]) -> List[int]:
    '''
    Sorts a list of integers using the merge sort algorithm.

    Args:
        input_list (List[int]): The list of integers to sort.

    Returns:
        List[int]: The sorted list.
    '''

    if len(input_list) <= 1:
        return input_list

    mid: int = len(input_list) // 2
    left_half: List[int] = merge_sort(input_list[:mid])
    right_half: List[int] = merge_sort(input_list[mid:])

    return _merge(left_half, right_half)


def _merge(left: List[int], right: List[int]) -> List[int]:
    '''
    Merges two sorted lists into a single sorted list.

    Args:
        left (List[int]): The first sorted list.
        right (List[int]): The second sorted list.

    Returns:
        List[int]: The merged and sorted list.
    '''

    merged = []

    i: int = 0
    j: int = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def read_input_from_file(file_name: str) -> Tuple[List[int], List[int]]:
    '''
    Reads the contents of a .txt file and returns it as a two lists of integers.

    Args:
        file_name (str): The name of the .txt file to be read.
    Returns:
        Tuple[List[int], List[int]]: Two lists of integers extracted from the file.
    '''

    try:
        file_path: Path = Path(__file__).parent / file_name
        with file_path.open('r', encoding='utf-8') as file:
            left_list, right_list = [], []

            for line in file:
                if not line.strip() or len(line.strip().split()) != 2:
                    continue

                left: List
                right: List

                left, right = map(int, line.strip().split())
                left_list.append(left)
                right_list.append(right)
        return left_list, right_list
    except FileNotFoundError as e:
        logging.error('File not found: %s, Error: %s', file_name, e)
