from pathlib import Path
from typing import List


def read_input_from_file(file_name: str) -> List[int]:
    '''
    Reads the contents of a .txt file and returns a list of integers.

    Args:
        file_name (str): The name of the .txt file to be read.
    Returns:
        str: The contents of the file.
    '''

    try:
        file_path: Path = Path(__file__).parent / file_name
        with file_path.open('r', encoding='utf-8') as file:
            return [[int(item) for item in line.split()] for line in file]
    except FileNotFoundError as e:
        logging.error('File not found: %s, Error: %s', file_name, e)
        raise


def is_safe(values: List[int]) -> bool:
    '''
    Checks if a list of integers is considered 'safe' based on specific rules.

    Args:
        values (List[int]): The list of integers to evaluate.
    Returns:
        bool: True if the list is 'safe', otherwise False.
    '''

    increasing: bool = all(values[i] < values[i + 1]
                            for i in range(len(values) - 1))
    decreasing: bool = all(values[i] > values[i + 1]
                            for i in range(len(values) - 1))
    differences_valid: bool = all(
        1 <= abs(values[i] - values[i + 1]) <= 3 for i in range(len(values) - 1))

    return (increasing or decreasing) and differences_valid
