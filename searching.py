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

def main():

    sequential_data = read_data('sequential.json', 'unordered_numbers')
    print(sequential_data)

    hledane = 8
    print(linear_search(sequential_data, hledane))

if __name__ == "__main__":

    main()
