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
