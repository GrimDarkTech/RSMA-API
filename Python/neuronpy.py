from enum import Enum
import math

class Activations(Enum):
    relu = 1
    sigmoid = 2
    
class Neuron:
    """Сlass that implements behavior similar to a nerve cell (neuron). Based on the mathematical model of the McCulloch—Pitts neuron"""
    
    inputs: list
    """Neuron input values"""
    weights: list
    """Neuron weights values"""
    activation:  Activations
    """Neuron activation function. Relu is default"""
    normalize: bool
    """If true, neuron input values will normalized from 0 to 1"""
    offset: float
    """Offset of neuron value"""
    output: float
    """Neuron input values"""
    error: float
    """Error variable for learning"""
    gradient: float
    """Gradient variable for learning"""
    initial_weights: float
    """Weights before network training"""
    
    def __init__(self, inputs, weights, activation, normalize):
        """Inits new neuron"""
        self.inputs = inputs
        self.weights = weights
        self.activation = activation
        self.normalize = normalize
        self.offset = 0
        self.output = 0
        self.error = 0
        self.gradient = 0
        self.initial_weights = []
    
    def calculate(self):
        """Calculates output value for neuron"""
        weightedInputs = [float]
        self.output = 0
        if(len(self.inputs) == len(self.weights)):
            if(self.normalize):
                for i in range(0, len(self.inputs)):
                    self.inputs[i] = self.inputs[i] / float(len(self.inputs))
            weightedInputs = self.inputs.copy()
            
            for i in range(0, len(weightedInputs)):
                weightedInputs[i] *= self.weights[i]
                self.output += weightedInputs[i]
            self.output += self.offset
            if(self.activation == Activations.sigmoid):
                self.output = 1 / (1 + math.pow(math.e, -self.output))
            elif(self.activation == Activations.relu):
                if(self.output < 0):
                    self.output = 0
        else:
            print("Error: Arrays of input values and weights have different lengths")
                
                
            
        
                
                
            
            
    