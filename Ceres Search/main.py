from typing import List, Tuple

import utils
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
            nx: int
            ny: int
            nx, ny = x + i * dx, y + i * dy

            if nx < 0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix[0]) or matrix[nx][ny] != word[i]:
                return False
        return True

    directions: List[Tuple[int]] = [
        (0, 1),   # Horizontal to the right
        (0, -1),  # Horizontal to the left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Main diagonal down
        (-1, -1), # Main diagonal up
        (1, -1),  # Secondary diagonal down
        (-1, 1)   # Secondary diagonal up
    ]

    world_count: int = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for dx, dy in directions:
                if search_direction(x, y, dx, dy):
                    world_count += 1
    return world_count


def main():
    try:
        input: List[str] = utils.read_input_from_file('input.txt')

        part_one_result: int = find_word_in_matrix(matrix=input, word='XMAS')
        logging.info('Part one result: %s', part_one_result)
    except Exception as e:
        logging.error('An error occurred: %s', e)


if __name__ == '__main__':
    main()
