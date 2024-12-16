from typing import Tuple
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def read_input_from_file(file_name: str) -> str:
    '''
    Reads the contents of a .txt file and returns it as a string.

    Args:
        file_name (str): The name of the .txt file to be read.
    Returns:
        str: The contents of the file.
    '''

    try:
        file_path: Path = Path(__file__).parent / file_name
        with file_path.open('r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as e:
        logging.error('File not found: %s, Error: %s', file_name, e)
        raise


def parse_mul_expression(expression: str) -> Tuple[int, int]:
    '''
    Parse a 'mul(x, y)' expression into a tuple of integers.

    Args:
        expression (str): The string of expression.
    Returns:
        Tuple[int, int]: The contents of the expression parsed.
    '''

    values = expression[4:-1].split(',')
    return (int(values[0]), int(values[1]))
