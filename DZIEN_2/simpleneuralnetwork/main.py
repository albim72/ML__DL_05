import numpy as np
from simplenn import SimpleNeuralNetwork

network = SimpleNeuralNetwork()
print(network.weights)

train_inputs = np.array([[1,1,0],[1,1,1],[1,1,0],[1,0,0],[0,1,1],[0,1,0]])
train_outputs = np.array([[0,1,0,0,1,0]]).T
train_iterators = 75000

network.train(train_inputs,train_outputs,train_iterators)
print(network.weights)

print("Testowanie sieci neuronowej")
testdata = np.array([[1,1,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[1,1,1],[0,0,0],[1,1,0],[0,1,1]])

for data in testdata:
    print(f"wynik testu dla {data} wynosi: {network.propagation(data)}")
n = len(testdata)#liczba przypadków
p = n-1 #liczba pozytywnych przypadków
accuracy = p/n
print(f"dokładność (ten przypadek): {accuracy}")

