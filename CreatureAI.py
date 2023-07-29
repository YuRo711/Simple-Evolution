from Node import *
from constants import *
import random


class CreatureAI:
    def __init__(self, parent=None):
        self.inner_nodes_x = []
        self.inner_nodes_y = []
        if parent is None:
            x_weights = np.ndarray(NODES)
            y_weights = np.ndarray(NODES)
            for i in range(NODES):
                self.inner_nodes_x.append(Node(np.array([random.random() - 0.5]),
                                       random.randint(-2, 2)))
                self.inner_nodes_y.append(Node(np.array([random.random() - 0.5]),
                                         random.randint(-2, 2)))
                x_weights[i] = random.random() - 0.5
                y_weights[i] = random.random() - 0.5
            self.x_node_out = Node(x_weights, random.randint(-2, 2))
            self.y_node_out = Node(y_weights, random.randint(-2, 2))
        else:
            x_mutations = [random.random() + 0.75 in range(NODES)]
            y_mutations = [random.random() + 0.75 in range(NODES)]
            self.inner_nodes_x = parent.inner_nodes_x
            self.inner_nodes_y = parent.inner_nodes_y
            self.x_node_out = parent.x_node_out
            self.x_node_out.w *= x_mutations
            self.y_node_out = parent.y_node_out
            self.y_node_out.w *= y_mutations

    def predict(self, X_x, X_y):
        Y_x = np.array([node.result(X_x) for node in self.inner_nodes_x])
        Y_y = np.array([node.result(X_y) for node in self.inner_nodes_y])
        x_res = -1 if self.x_node_out.result(Y_x) < 0 else 1
        y_res = -1 if self.y_node_out.result(Y_y) < 0 else 1
        return x_res, y_res
