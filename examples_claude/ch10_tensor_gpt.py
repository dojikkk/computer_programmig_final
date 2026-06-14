class Layer:
    def forward(self, x):
        raise NotImplementedError("Subclasses must implement forward().")
    def __call__(self, x):
        return self.forward(x)
    
class Linear(Layer):
    def __init__(self, input_dim, output_dim):
        self.input_dim = int(input_dim)
        self.output_dim = int(output_dim)
        self.weights = []
        for i in range(self.output_dim):
            inputing = input(f'Enter weight row {i+1}: ')
            if len(inputing.split()) != int(self.input_dim):
                raise IndexError('인풋값과 입력된 값이 맞지 않습니다')
            else:
                self.weights.append(list(map(float, inputing.split())))

        inputing = input('Enter bias: ')
        if len(inputing.split()) != int(output_dim):
            raise IndexError('bias와 출력크기가 맞지 않습니다')
        else:
            self.bias = list(map(int, inputing.split()))

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
            output.append(total + self.bias[i])
        
        return output
    
    def __repr__(self):
        return f"Linear(input_dim={self.input_dim}, output_dim={self.output_dim})"

class ReLU(Layer):
    def forward(self, x):
        # 음수를 0으로 바꾸는건 max 함수를 활용하면 된다
        return [max(0, k) for k in x]

class Sequential:
    """
    A container that applies layers sequentially.
    """

    def __init__(self, *layers):
        self.layers = list(layers)
    
    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x
    
    def __call__(self, x):
        return self.forward(x)

a, b = input('Enter input_dim and output_dim: ').split()

first = Linear(a, b)

y = input('Enter input vector: ').split()
vector = list(map(int, y))

alpha = Sequential(first, ReLU())

print(alpha(vector))