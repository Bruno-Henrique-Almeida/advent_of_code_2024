from pathlib import Path
import re


def extract_and_calculate_multiplications(input_string: str) -> int:
    '''
    Extracts specific patterns from the input string and calculates the sum of the product of the extracted integers.

    Args:
        input_string (str): The string to process.
    Returns:
        int: The calculated sum of the absolute products.
    '''

    regex = r'(mul\(\w+,\w+\))'

    matches = re.findall(regex, input_string)

    sanitized_matches = [eval(x.replace('mul', '')) for x in matches]

    return sum(abs(item[0] * item[1]) for item in sanitized_matches)


def extract_and_calculate_enabled_multiplications(input_string: str) -> int:
    '''
    Extracts specific enabled patterns from the input string and calculates the sum of the product of the extracted integers.

    Args:
        input_string (str): The string to process.
    Returns:
        int: The calculated sum of the absolute products.
    '''

    regex = r"(don't\(\))|(do\(\))|(mul\(\w+,\w+\))"

    matches = re.findall(regex, input_string)

    ignore_mul = False

    captured = []

    for match in matches:
        if match[0] == "don't()":
            ignore_mul = True
        elif match[1] == "do()":
            ignore_mul = False
        elif match[2].startswith("mul") and not ignore_mul:
            captured.append(match[2])

    sanitized_enabled_matches = [eval(x.replace('mul', '')) for x in captured]

    return sum(abs(item[0] * item[1]) for item in sanitized_enabled_matches)


def read_list_from_file(file_name: str) -> str:
    file_path = Path(__file__).parent / file_name
    with file_path.open('r', encoding='utf-8') as file:
        return file.read()


input = read_list_from_file('input.txt')

# Part one | Expected result: 165,225,049
response = extract_and_calculate_multiplications(input)
print(f'Part one result: {response}')

# Part two | Expected result: 108,830,766
response = extract_and_calculate_enabled_multiplications(input)
print(f'Part two result: {response}')
