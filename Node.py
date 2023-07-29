import numpy as np


class Node:
    def __init__(self, w: np.array, b):
        self.w = w
        self.b = b

    def result(self, X: np.array):
        return X.flatten().dot(self.w) + self.b
