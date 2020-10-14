from helper import parse_args, read_data

if __name__ == '__main__':
    input, output = parse_args()
    features, labels = read_data(input)
    print(features, labels)
