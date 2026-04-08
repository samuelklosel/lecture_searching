import time
from pathlib import Path
import json
import generators


from generators import dna_sequence


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
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)

        if field == "unordered_numbers":
            result = data[field]
            return result
        if field == "ordered_numbers":
            result = data[field]
            return result
        if field == "dna_sequence":
            result = data[field]
            return str(result)
        else:
            return None

def linear_search(data, number):
    slovnik = {}
    positions = []
    i = 0
    count = 0
    for value in data:
        if data[i] == number:
            count += 1
            positions.append(i)
        i += 1
    result = {"positions": positions, "count": count}
    return result

def binary_search(data, number):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == number:
            return mid
        if data[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return None

def main(file_name, field, number, searching):
    data = read_data(file_name, field)
    if searching == "linear":
        search = linear_search(data, number)
    if searching == "binary":
        search = binary_search(data, number)
    return search


if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000, 10000]
    linear_times = []
    binary_times = []
    for size in sizes:
        start = time.perf_counter()
        linear_search(size, 8)
        end = time.perf_counter()
        duration = end - start
    if searching == "linear":
        linear_times.append(duration)
    if searching == "binary":
        binary_times.append(duration)
    print(main("sequential.json", "ordered_numbers", 14, "binary"))
    start = time.perf_counter()
    end = time.perf_counter()
    duration = end - start
    print(f"Měření trvalo: {duration:.8f} s")
