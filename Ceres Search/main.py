from pathlib import Path
from typing import List

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def find_word_in_matrix(matrix: List[List[str]], word: str = 'XMAS') -> int:
    '''
    Count occurrences of a word in a matrix in all 8 possible directions.

    Args:
        matrix (list[list[str]]): A 2D list representing the matrix of letters.
        word (str): The word to search for in the matrix.
    Returns:
        int: The number of times the word is found in the matrix.
    '''

    def search_direction(x: int, y: int, dx: int, dy: int):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy

            if nx < 0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix[0]) or matrix[nx][ny] != word[i]:
                return False
        return True

    directions = [
        (0, 1),   # Horizontal to the right
        (0, -1),  # Horizontal to the left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Main diagonal down
        (-1, -1), # Main diagonal up
        (1, -1),  # Secondary diagonal down
        (-1, 1)   # Secondary diagonal up
    ]

    count = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for dx, dy in directions:
                if search_direction(x, y, dx, dy):
                    count += 1
    return count


def read_input_from_file(file_name: str) -> List[List[str]]:
    '''
    Reads the contents of a .txt file and returns it as 2D lists of matrix.

    Args:
        file_name (str): The name of the .txt file to be read.
    Returns:
        List[List[str]]: The 2D lists of matrix extracted from the file.
    '''
    try:
        file_path = Path(__file__).parent / file_name
        matrix = []

        with file_path.open('r', encoding='utf-8') as file:
            file_content = file.read()
            for line in file_content.split():
                matrix.append([letter for letter in line])
            return matrix
    except FileNotFoundError as e:
        logging.error('An error occurred: %s', e)


def main():
    try:
        input = read_input_from_file('input.txt')

        # Part one | Expected result: 2.336
        part_one_result = find_word_in_matrix(matrix=input, word='XMAS')
        logging.info('Part one result: %s', part_one_result)

    except Exception as e:
        logging.error('An error occurred: %s', e)


if __name__ == '__main__':
    main()
