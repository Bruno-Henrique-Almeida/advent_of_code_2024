from typing import Pattern, List, Tuple, Generator
import logging
import utils
import re

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def extract_and_calculate_multiplications(input_string: str) -> int:
    '''
    Extracts specific patterns from the input string and calculates the sum of the product of the extracted integers.

    Args:
        input_string (str): The string to process.
    Returns:
        int: The calculated sum of the absolute products.
    '''

    regex: Pattern[str] = r'(mul\(\w+,\w+\))'
    matches: Generator = (match.group()
                          for match in re.finditer(regex, input_string))

    parsed_values: Generator = (
        utils.parse_mul_expression(match) for match in matches)

    return sum(abs(a * b) for a, b in parsed_values)


def extract_and_calculate_enabled_multiplications(input_string: str) -> int:
    '''
    Extracts specific enabled patterns from the input string and calculates the sum of the product of the extracted integers.

    Args:
        input_string (str): The string to process.
    Returns:
        int: The calculated sum of the absolute products.
    '''

    regex: Pattern = r"(don't\(\))|(do\(\))|(mul\(\w+,\w+\))"
    matches: Generator = (match.group()
                          for match in re.finditer(regex, input_string))

    ignore_mul: bool = False
    captured: List = []

    for match in matches:
        if match == "don't()":
            ignore_mul = True
            continue
        if match == 'do()':
            ignore_mul = False
            continue
        if match.startswith('mul') and not ignore_mul:
            captured.append(match)

    parsed_values: Generator = (
        utils.parse_mul_expression(match) for match in captured)

    return sum(abs(a * b) for a, b in parsed_values)


def main():
    try:
        input: str = utils.read_input_from_file('input.txt')

        part_one_result: int = extract_and_calculate_multiplications(input)
        logging.info('Part one result: %s', part_one_result)

        part_two_result: int = extract_and_calculate_enabled_multiplications(
            input)
        logging.info('Part tow result: %s', part_two_result)
    except Exception as e:
        logging.error('An error occurred: %s', e)


if __name__ == '__main__':
    main()
