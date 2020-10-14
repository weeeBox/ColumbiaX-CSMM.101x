def parse_args():
    import sys
    return sys.argv[1], sys.argv[2]


def read_input(path):
    import csv
    with open(path, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        return [(int(feature_1), int(feature_2), int(label)) for feature_1, feature_2, label in reader]


if __name__ == '__main__':
    input, output = parse_args()
    data = read_input(input)
    print(data)
