from msilib import make_id
from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    povolene_fieldy = {'unordered_numbers', 'ordered_numbers', 'dna_sequence'}

    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

    with open(file_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
        if field not in povolene_fieldy:
            return None
        return data.get(field)

def linear_search(sequence, searched_number):

    positions = []

    for i, number in enumerate(sequence):
        if number == searched_number:
            positions.append(i)
    count = len(positions)

    return {"positions": positions, "count": count}

def binary_search(sequence, searched_number):

    left = 0
    right = len(sequence) - 1

    while left <= right:

        mid = (left + right) // 2
        mid_hodnota = sequence[mid]

        if mid_hodnota == searched_number:
            return mid
        elif mid_hodnota < searched_number:
            left = mid + 1
        else:
            right = mid - 1

    return None

def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    hledane = 8
    print(linear_search(sequential_data, hledane))

    sequential_data_un = read_data("sequential.json", "ordered_numbers")

    nase = 14
    print(binary_search(sequential_data_un, nase))

if __name__ == "__main__":

    main()
