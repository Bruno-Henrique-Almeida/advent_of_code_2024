from typing import Tuple, List, Pattern, Generator
from pathlib import Path
import re
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def read_input_from_file(file_name: str) -> Tuple[List[List[int]], List[List[int]]]:
    '''
    Reads the contents of a .txt file and returns it as a tuple of lists

    Args:
        file_name (str): The name of the .txt file to be read.
    Returns:
        Tuple[List[List[int]], List[List[int]]]: The contents of the file.
    '''

    try:
        file_path: Path = Path(__file__).parent / file_name
        with file_path.open('r', encoding='utf-8') as file:
            content = file.read()
            
            regex: Pattern = r'(\d+)\|(\d+)'
            matches: Generator = (match.group() for match in re.finditer(regex, content))
            pages: List[List[int]] = [list(map(int, page.split('|'))) for page in matches]

            regex: Pattern = r"^\d+(?:,\d+)*$"
            matches: Generator = (match.group() for match in re.finditer(regex, content, re.MULTILINE))
            values: List[List[int]] = [list(map(int, match.split(','))) for match in matches]
        return pages, values
    except FileNotFoundError as e:
        logging.error('File not found: %s, Error: %s', file_name, e)
        raise
