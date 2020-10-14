from helper import parse_args, read_data
import numpy as np


def predict(X, W):
    return np.sign(np.sum(np.multiply(X, W)))


if __name__ == '__main__':
    input, output = parse_args()

    # read training data
    X, Y = read_data(input)

    n, d = X.shape  # number of training examples and features

    # initialize weights with 0
    W = np.zeros(d)

    result = np.empty(shape=(0, d), dtype=np.int)

    # repeat until convergence
    while True:
        converged = True
        for i in range(n):
            x, y = X[i], Y[i]
            y_pred = predict(x, W)

            if y * y_pred <= 0:  # misclassified?
                converged = False
                for j in range(d):
                    W[j] += y * x[j]

        if converged:
            break

        result = np.row_stack((result, W))

    np.savetxt(fname=output, X=result, fmt='%d', delimiter=",")
