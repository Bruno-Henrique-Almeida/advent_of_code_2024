from pathlib import Path


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
