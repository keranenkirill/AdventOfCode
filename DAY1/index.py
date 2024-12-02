def read_file_to_lists(filename):
    """Reads the file and splits values into two lists."""
    list1 = []
    list2 = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.split()
            # split values per line into two lists
            list1.append(int(values[0]))
            list2.append(int(values[1]))
    return list1, list2


def sort_list(list1, list2):
    list1.sort()
    list2.sort()
    return list1, list2


def calculate_total_distance(list1, list2):
    list1, list2 = sort_list(list1, list2)
    total_distance = 0

    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])

    print(total_distance)
    return total_distance


if __name__ == "__main__":
    filename = "input.txt"
    List1, List2 = read_file_to_lists(filename)

    Result = calculate_total_distance(List1, List2)
