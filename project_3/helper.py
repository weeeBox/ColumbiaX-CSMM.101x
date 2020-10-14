import numpy as np


def parse_args():
    import sys
    return sys.argv[1], sys.argv[2]


def read_data(path):
    """
    Reads training data with labels
    :param path: csv file path
    :return: X, Y where X - training data, Y - labels
    """
    dataset = np.genfromtxt(path, delimiter=',')
    n = dataset.shape[0]
    X = np.column_stack((dataset[:, :-1], np.ones(shape=(n,))))
    Y = dataset[:, -1]
    return X, Y
