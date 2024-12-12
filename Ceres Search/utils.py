from pathlib import Path
from typing import List


def read_input_from_file(file_name: str) -> List[List[str]]:
    '''
    Reads the contents of a .txt file and returns it as 2D lists of matrix.

    Args:
        file_name (str): The name of the .txt file to be read.
    Returns:
        List[List[str]]: The 2D lists of matrix extracted from the file.
    '''

    try:
        file_path: Path = Path(__file__).parent / file_name
        matrix: List = []

        with file_path.open('r', encoding='utf-8') as file:
            file_content: str = file.read()
            for line in file_content.split():
                matrix.append([letter for letter in line])
            return matrix
    except FileNotFoundError as e:
        logging.error('An error occurred: %s', e)
