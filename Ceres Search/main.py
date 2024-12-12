from typing import List, Tuple
import logging
import utils

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def find_word_in_matrix(matrix: List[List[str]], word: str = 'XMAS') -> int:
    '''
    Count occurrences of a word in a matrix in all 8 possible directions.

    Args:
        matrix (list[list[str]]): A 2D list representing the matrix of letters.
        word (str): The word to search for in the matrix.
    Returns:
        int: The number of times the word is found in the matrix.
    '''

    def search_in_direction(x: int, y: int, dx: int, dy: int, word: str) -> bool:
        '''
        Check if the word exists in a specific direction starting at (x, y).

        Args:
            x (int): The starting row index.
            y (int): The starting column index.
            dx (int): The direction vector for row movement.
            dy (int): The direction vector for column movement.
            word (str): The word to check for.

        Returns:
            bool: True if the word is found, False otherwise.
        '''

        word_length: int = len(word)
        end_x, end_y = x + (word_length - 1) * dx, y + (word_length - 1) * dy

        if not (0 <= end_x < len(matrix) and 0 <= end_y < len(matrix[0])):
            return False

        return all(matrix[x + i * dx][y + i * dy] == word[i] for i in range(word_length))

    directions: List[Tuple[int, int]] = [
        (0, 1),  # Horizontal to the right
        (0, -1),  # Horizontal to the left
        (1, 0),  # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),  # Main diagonal down
        (-1, -1),  # Main diagonal up
        (1, -1),  # Secondary diagonal down
        (-1, 1)  # Secondary diagonal up
    ]

    word_count: int = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for dx, dy in directions:
                if search_in_direction(x, y, dx, dy, word):
                    word_count += 1

    return word_count


def find_x_shape_in_matrix(matrix: List[List[str]]) -> int:
    '''
    Count occurrences of "X" shapes in a matrix, where the center is 'A' and the corners match specific patterns.

    Args:
        matrix (List[List[str]]): A 2D list of strings representing the matrix to be searched.

    Returns:
        int: The count of "X" shapes found in the matrix.
    '''

    valid_patterns: set = {'MMSS', 'MSSM', 'SSMM', 'SMMS'}
    word_count: int = 0

    for x in range(1, len(matrix) - 1):
        for y in range(1, len(matrix[0]) - 1):
            if matrix[x][y] != 'A':
                continue

            corners = ''.join([
                matrix[x - 1][y - 1],
                matrix[x - 1][y + 1],
                matrix[x + 1][y + 1],
                matrix[x + 1][y - 1],
            ])

            if corners in valid_patterns:
                word_count += 1

    return word_count


def main():
    try:
        input_matrix: List[str] = utils.read_input_from_file('input.txt')

        part_one_result: int = find_word_in_matrix(
            matrix=input_matrix, word='XMAS')
        logging.info('Part one result: %s', part_one_result)

        part_two_result: int = find_x_shape_in_matrix(
            matrix=input_matrix)
        logging.info('Part two result: %s', part_two_result)
    except Exception as e:
        logging.error('An error occurred: %s', e)


if __name__ == '__main__':
    main()
