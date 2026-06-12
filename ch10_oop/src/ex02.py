import math
import random


class Layer:
    """
    Base class for all neural network layers.
    """

    def forward(self, x):
        raise NotImplementedError("Subclasses must implement forward().")

    def __call__(self, x):
        return self.forward(x)

class Linear(Layer):
    """
    Linear layer.
    Input:
        x: list of numbers, shape = [input_dim]
    Output:
        y: list of numbers, shape = [output_dim]
    Formula:
        y = Wx + b
    """
    def __init__(self, input_dim, output_dim):
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.weights = []
        for i in range(output_dim):
            row = []
            for j in range(input_dim):
                row.append(random.uniform(-1.0, 1.0))
            self.weights.append(row)
        self.bias = []

        for i in range(output_dim):
            self.bias.append(random.uniform(-1.0, 1.0))

    def forward(self, x):
        if len(x) != self.input_dim:
            raise ValueError(
                f"Expected input size {self.input_dim}, but got {len(x)}."
            )
        output = []

        for i in range(self.output_dim):
            total = 0
            for j in range(self.input_dim):
                total += self.weights[i][j] * x[j]
            total += self.bias[i]
            output.append(total)

        return output

    def __repr__(self):
        return f"Linear(input_dim={self.input_dim}, output_dim={self.output_dim})"


class ReLU(Layer):
    """
    ReLU activation layer.
    """
    def forward(self, x):
        return [max(0, value) for value in x]
    def __repr__(self):
        return "ReLU()"


class Sigmoid(Layer):
    """
    Sigmoid activation layer.
    """

    def forward(self, x):
        return [1 / (1 + math.exp(-value)) for value in x]

    def __repr__(self):
        return "Sigmoid()"


class Sequential:
    """
    A container that applies layers sequentially.
    """

    def __init__(self, *layers):
        self.layers = list(layers)

    def add(self, layer):
        if not isinstance(layer, Layer):
            raise TypeError("Only Layer objects can be added.")
        self.layers.append(layer)

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def __call__(self, x):
        return self.forward(x)

    def summary(self):
        print("Model Summary")
        print("-------------")
        for i, layer in enumerate(self.layers):
            print(f"{i + 1}. {layer}")

            if isinstance(layer, Linear):
                print("   weights =", layer.weights)
                print("   bias    =", layer.bias)

    def __repr__(self):
        return f"Sequential({self.layers})"


# Example usage
model = Sequential(
    Linear(input_dim=3, output_dim=4),
    ReLU(),
    Linear(input_dim=4, output_dim=2),
    Sigmoid()
)

x = [1.0, 2.0, -1.0]

model.summary()

output = model(x)

print()
print("Input:", x)
print("Output:", output)
