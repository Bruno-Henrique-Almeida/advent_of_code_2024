from typing import List, Tuple
from pathlib import Path


def merge_sort(input_list: List[int]) -> List[int]:
    if len(input_list) > 1:
        mid: int = len(input_list) // 2
        left_half: List[int] = input_list[:mid]
        right_half: List[int] = input_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i: int = 0
        j: int = 0
        k: int = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                input_list[k] = left_half[i]
                i += 1
            else:
                input_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            input_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            input_list[k] = right_half[j]
            j += 1
            k += 1
    return input_list


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
