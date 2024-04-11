from layerpy import Layer

class Network:
    "Contains a list of neuron layers"
    
    inputs: list
    """Input layer"""
    layers: list
    """List of layers in neural network"""
    outputs: list
    """Network output value"""

    def __init__(self, layers):
        self.layers = layers
        self.outputs = []
        self.inputs = []

    def calculate(self):
        """Calculates output values for network"""
        self.layers[0].set_inputs(self.inputs)
        self.layers[0].calculate()
        for i in range(1, len(self.layers) - 1):
            self.layers[i].set_inputs(self.layers[i - 1].outputs)
            self.layers[i].calculate()
        
        if(len(self.layers) > 1):
            self.layers[len(self.layers) - 1].set_inputs(self.layers[len(self.layers) - 2].outputs)
            self.layers[len(self.layers) - 1].calculate()
        self.outputs = self.layers[len(self.layers) - 1].outputs

    def learn(self, target_values: list, learning_rate: float, epochs: int):
        """Learns network using backpropagation"""

        for e in range(0, epochs):
            #Calculate network
            self.calculate()

            #Error and gradient for output layer
            layer = self.layers[len(self.layers) - 1]
            
            for n in range(0, len(layer.neurons)):
                neuron = layer.neurons[n]
                neuron.error = neuron.output - target_values[n]
                neuron.gradient = neuron.error * neuron.output * (1 - neuron.output)
                neuron.initial_weights = []

                for w in range(0, len(neuron.weights)):
                    neuron.initial_weights.append(neuron.weights[w])
                    neuron.weights[w] = neuron.weights[w] - learning_rate * neuron.gradient * neuron.output



                layer.neurons[n] = neuron

            #Error and gradient for other layers
            for l in range(len(self.layers) - 2, 0):

                for n in range(0, len(self.layers[l].neurons) - 1):
                    neuron = self.layers[l].neurons[n]
                    neuron.error = 0

                    for k in range(0, len(self.layers[l + 1].neurons)):
                        neuron.error += self.layers[l + 1].neurons[k].initial_weights[n] * self.layers[l + 1].neurons[k].gradient
                    neuron.gradient = neuron.error * neuron.output * (1 - neuron.output)

                    for w in range(0, len(neuron.weights)):
                        neuron.initial_weights.append(neuron.weights[w])
                        neuron.weights[w] = neuron.weights[w] - learning_rate * neuron.gradient * neuron.output

                