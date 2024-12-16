from typing import List
import logging
import utils

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_middle_sum(values: List[List[int]], pages: List[List[int]]) -> int:
    '''
    Calculates the sum of the central elements of the lists that meet specific conditions.

    Args:
        values (list of lists): A list containing lists of values.
        pages (list of lists): A list of pages with relationships between the values.
    Returns:
        int: The sum of the central elements of the lists that meet the conditions.
    '''

    total_sum = 0

    for value in values:
        matching_elements = []
        for item in value:
            relevant_pages = [
                page for page in pages if item in page and all(x in value for x in page)
            ]

            valid = all(
                value.index(page[0]) < value.index(page[1]) for page in relevant_pages
            )

            if valid and item not in matching_elements:
                matching_elements.append(item)

        if matching_elements == value:
            mid = len(matching_elements) // 2
            total_sum += matching_elements[mid]

    return total_sum


def calculate_corrected_middle_sum(values: List[List[int]], pages: List[List[int]]) -> int:
    '''
    Calculates the sum of the central elements of the lists that meet specific conditions.

    Args:
        values (list of lists): A list containing lists of values.
        pages (list of lists): A list of pages with relationships between the values.
    Returns:
        int: The sum of the central elements of the lists that meet the conditions.
    '''

    total_sum: int = 0
    lists_to_correct: List = []
    corrected_lists: List = []

    for value_list in values:
        temp_result = []
        for value in value_list:
            relevant_pages = [
                page for page in pages if value in page and all(x in value_list for x in page)
            ]

            is_valid = all(
                value_list.index(page[0]) < value_list.index(page[1]) for page in relevant_pages
            )

            if is_valid and value not in temp_result:
                temp_result.append(value)

        if temp_result != value_list:
            lists_to_correct.append(value_list)

    for value_list in lists_to_correct:
        corrected_list = value_list.copy()
        for value in value_list:
            for page in pages:
                if all(x in corrected_list for x in page):
                    pos1, pos2 = corrected_list.index(page[0]), corrected_list.index(page[1])

                    if pos1 > pos2:
                        corrected_list[pos1], corrected_list[pos2] = corrected_list[pos2], corrected_list[pos1]
        corrected_lists.append(corrected_list)

    for corrected_list in corrected_lists:
        if corrected_list:
            mid = len(corrected_list) // 2
            total_sum += corrected_list[mid]

    return total_sum


def main():
    try:
        input_pages, input_values = utils.read_input_from_file('input.txt')

        part_one_result: int = calculate_middle_sum(input_values, input_pages)
        logging.info('Part one result: %s', part_one_result)

        part_two_result: int = calculate_corrected_middle_sum(input_values, input_pages)
        logging.info('Part two result: %s', part_two_result)
    except Exception as e:
        logging.error('And error occurred: %s', e)


if __name__ == '__main__':
    main()
