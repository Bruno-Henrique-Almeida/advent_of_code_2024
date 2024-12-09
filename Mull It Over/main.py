from typing import Pattern, List, Tuple
import utils
import re

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def extract_and_calculate_multiplications(input_string: str) -> int:
    '''
    Extracts specific patterns from the input string and calculates the sum of the product of the extracted integers.

    Args:
        input_string (str): The string to process.
    Returns:
        int: The calculated sum of the absolute products.
    '''

    regex: Pattern[str] = r'(mul\(\w+,\w+\))'

    matches: List[str] = re.findall(regex, input_string)

    sanitized_matches: List[Tuple] = [eval(x.replace('mul', '')) for x in matches]

    return sum(abs(item[0] * item[1]) for item in sanitized_matches)


def extract_and_calculate_enabled_multiplications(input_string: str) -> int:
    '''
    Extracts specific enabled patterns from the input string and calculates the sum of the product of the extracted integers.

    Args:
        input_string (str): The string to process.
    Returns:
        int: The calculated sum of the absolute products.
    '''

    regex: Pattern = r"(don't\(\))|(do\(\))|(mul\(\w+,\w+\))"

    matches: re.Pattern = re.findall(regex, input_string)

    ignore_mul: bool = False

    captured: List = []

    for match in matches:
        if match[0] == "don't()":
            ignore_mul = True
        elif match[1] == "do()":
            ignore_mul = False
        elif match[2].startswith("mul") and not ignore_mul:
            captured.append(match[2])

    sanitized_enabled_matches: List[Tuple] = [eval(x.replace('mul', '')) for x in captured]

    return sum(abs(item[0] * item[1]) for item in sanitized_enabled_matches)


def main():
    try:
        input: str = utils.read_input_from_file('input.txt')

        part_one_result: int = extract_and_calculate_multiplications(input)
        logging.info('Part one result: %s', part_one_result)

        part_two_result: int = extract_and_calculate_enabled_multiplications(input)
        logging.info('Part tow result: %s', part_two_result)
    except Exception as e:
        logging.error('An error occurred: %s', e)


if __name__ == '__main__':
    main()
