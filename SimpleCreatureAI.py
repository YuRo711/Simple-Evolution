from Node import *
from constants import *
import random


class SimpleCreatureAI:
    def __init__(self, parent=None):
        if parent is None:
            self.node_x = Node(np.array([random.random() - 0.5]),
                                       random.randint(-2, 2))
            self.node_y = Node(np.array([random.random() - 0.5]),
                               random.randint(-2, 2))
        else:
            self.node_x = parent.node_x
            self.node_y = parent.node_y
            x_mutation = random.random() + 0.75
            y_mutation = random.random() + 0.75
            self.node_x.w *= x_mutation
            self.node_y.w *= y_mutation

    def predict(self, Xx, Xy):
        x_res = -1 if self.node_x.result(Xx) < 0 else 1
        y_res = -1 if self.node_y.result(Xy) < 0 else 1
        return x_res, y_res
