from neuronpy import Neuron
from neuronpy import Activations

import random

class Layer:
    """Contains a list of neurons"""

    neurons: list
    """List of neurons contained in layer"""
    outputs: list
    """List of output values of neurons contained in layer"""
        
    def __init__(self, **kwargs):
        self.neurons = kwargs.get('neurons', [])
        number_of_neurons = kwargs.get('number_of_neurons', 0)
        number_of_inputs = kwargs.get('number_of_inputs', 0)
        activation = kwargs.get('activation', Activations.sigmoid)
        normalize = kwargs.get('normalize', False)

        if(number_of_neurons != 0):
            for i in range(0, number_of_neurons):
                weights = []
                inputs = []
                for j in range(0, number_of_inputs):
                    weights.append(random.random())
                    inputs.append(1)
                neuron = Neuron(inputs, weights, activation, normalize)
                self.neurons.append(neuron)
        self.outputs = []
    
    def set_inputs(self, inputs: list):
        """Sets input values for layer"""
        for i in range(len(self.neurons)):
            self.neurons[i].inputs = inputs.copy()
    
    def calculate(self):
        """Calculates output values for layer"""
        self.outputs = []
        for neuron in self.neurons:
            neuron.calculate()
            self.outputs.append(neuron.output)

    def calculate_kohonin(self):
        """Calculates output values for Kohonin layer"""
        self.outputs = []
        for neuron in self.neurons:
            neuron.calculate()

        max = self.neurons[0].output
        for n in range(0, len(self.neurons)):
            if(self.neurons[n].output >= max):
                max = self.neurons[n].output
        for neuron in self.neurons:
            if(neuron.output == max):
                self.outputs.append(neuron.output)
            else:
                self.outputs.append(0)
            
            