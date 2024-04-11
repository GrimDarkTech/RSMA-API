from neuronpy import Neuron
from neuronpy import Activations

from layerpy import Layer  

from networkpy import Network

import time

from rsmapy import RSMA

from rsma_client import RSMAClient

def main():

#Creating layers

    layers = []

    layer = Layer(number_of_neurons = 2, number_of_inputs = 6, activation = Activations.sigmoid, normalize = False)
    layers.append(layer)

    layer = Layer(number_of_neurons = 4, number_of_inputs = 2, activation = Activations.sigmoid, normalize = False)
    layers.append(layer)

    layer = Layer(number_of_neurons = 2, number_of_inputs = 4, activation = Activations.sigmoid, normalize = False)
    layers.append(layer)

    #Creating network
    network = Network(layers)
    network.inputs = [0, 0, 0, 0, 0, 0]

    x = 2
    y = 0.033
    z = 2
    
    motors = []

    #connecting to RSMA
    RSMA.connect("127.0.0.1","RSMApy")
    #waiting 1 second
    time.sleep(0.1)

    #sending command to RSMA
    RSMA.load_scene("SupremeFlat")
    time.sleep(0.1)

    RSMA.add_robot("DarkieBot_Altushka", 2, 0.1, 5, 0, 0, 0)
    time.sleep(0.1)

    RSMA.set_drone_control(0, True)
    time.sleep(0.1)

    RSMA.writer_start(0)
    time.sleep(0.1)

    for i in range (0, 100):
        RSMA.controller_position(0)
        time.sleep(0.02)
        input = []
        input.append(float(RSMAClient.controllers[0][1]))
        input.append(float(RSMAClient.controllers[0][2]))
        input.append(float(RSMAClient.controllers[0][3]))
        input.append(x)
        input.append(y)
        input.append(z)

        network.inputs = input
        network.calculate()
    
        RSMA.gpio_write(0, "PA", "1", 1)
        time.sleep(0.02)
        RSMA.gpio_write(0, "PB", "1", 1)
        time.sleep(0.02)

        RSMA.gpio_write(0, "PA", "3", network.outputs[0])
        time.sleep(0.02)
        RSMA.gpio_write(0, "PB", "3", network.outputs[1])
        time.sleep(0.02)
        time.sleep(0.2)

        print(network.outputs)

    RSMA.gpio_write(0, "PA", "3", 0)
    time.sleep(0.1)
    RSMA.gpio_write(0, "PB", "3", 0)
    time.sleep(0.1)

    RSMA.writer_stop(0)
    time.sleep(0.1)
    time.sleep(1)
    #disconnecting to RSMA
    RSMA.disconnect()


if __name__ == '__main__':
    main()