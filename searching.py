from pathlib import Path
import json
import time
import matplotlib.pyplot as plt


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

from generators import ordered_sequence

def compare_search():

    sizes = [100, 500, 1000, 5000, 10000]
    cycles = 100
    linear_times = []
    binary_times = []
    hop = 2000

    for size in sizes:
        sequence_o = ordered_sequence(size)
        start = time.perf_counter()
        for i in range(cycles):
            linear_search(sequence_o, hop)
            break

        end = time.perf_counter()
        duration = end - start

        linear_times.append(duration)

        start = time.perf_counter()
        for i in range(cycles):
            binary_search(sequence_o, hop)
            break

        end = time.perf_counter()
        duration = end - start

        binary_times.append(duration)


    plt.plot(sizes, linear_times)
    plt.plot(sizes, binary_times)

    plt.xlabel("Porovnání algoritmů")
    plt.ylabel("Čas [s]")
    plt.title("Ukázkový graf měření")
    plt.show()


def pattern_search(sequence, pattern):

    positions = []
    match = False

    for i in range(sequence):
        for k, d in enumerate(pattern):
            if sequence[i+k] == pattern[d]:
                match = True
            else:
                match = False
                break
        if match:
            positions.append(i)
        match = False
    return positions



def main():

    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)

    hledane = 8
    print(linear_search(sequential_data, hledane))

    sequential_data_un = read_data("sequential.json", "ordered_numbers")

    nase = 14
    print(binary_search(sequential_data_un, nase))

    compare_search()

if __name__ == "__main__":

    main()
