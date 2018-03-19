import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math


import logicGates

#pylint: disable=E1101

'''
La meta de este programa es programar
la regla de aprendizaje del perceptron
y la regla delta
'''
fig = plt.figure()
plt.axis([-3, 3, -3, 3])
plt.grid(True)
fig.suptitle('Delta')

gateString = ""#input('Compuerta (and, or, nand, nor): ')
gate = logicGates.andGate()#logicGates.getGate(gateString)
numEpocas = 1 #int(input('Numero maximo de epocas: '))
error = 0 #float(input('Error minimo: '))

for element in gate:
  if element[2] == 1:
    group = 'bo'
  else:
    group = 'ro'

  plt.plot(element[0], element[1], group)




''' Inicializar W [1, pesos], b, learning rate  '''
w = np.array([[0.1, 0.3]])
b = 0.1
alfa = 0.0001

e = 0

for x in range(numEpocas):
  for row in gate:
    p = np.array([row[:2]]).T
    t = int (row[2])

    a = np.dot(w, p)+ b
    #print(f"a: {a}")
    e = ((t - a)**2)/2

    w = w + (2*alfa*e*p).T
    #print(f"e {e}")
    b = b + 2*alfa*e
    #print(f"salida {a}")
    #print(f"target {t}")
  if e <= 0.1:
    print("aqui")
    break



w = w[0]
x = range(-3,3,1)
y = (-b-(w[0]*x))/w[1]
plt.plot(x, y)



print(w[0])
print(w[1])
print(b)









plt.show()
