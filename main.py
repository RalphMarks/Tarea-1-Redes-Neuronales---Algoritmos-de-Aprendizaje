import numpy as np
import matplotlib
import matplotlib.pyplot as plt

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
fig.suptitle('Perceptron')

gateString = input('Compuerta (and, or, nand, nor): ')
gate = logicGates.getGate(gateString)
numEpocas = int(input('Numero maximo de epocas: '))
error = float(input('Error minimo: '))

for element in gate:
  if element[2] == 1:
    group = 'bo'
  else:
    group = 'ro'

  plt.plot(element[0], element[1], group)




''' Inicializar W [1, pesos], b, learning rate  '''
w = np.array([[0.5, 0.5]])
b = 0.5
alfa = 0.001
errorList = []

for x in range(numEpocas):
  for row in gate:
    p = np.array([row[:2]]).T
    t = row[2]
    #print(f"p {p}")
    #print(f"t {t}")
    if (np.dot(w, p) + b) >= 0:
      a = 1
    else:
      a = 0

    e = t - a
    errorList.append(e)

    w = w + (alfa*e*p).T
    #print(f"e {e}")
    b = b + e
    #print(f"salida {a}")
    #print(f"target {t}")
  if e <= error:
    print(f"El error minimo se alcanzo: {e}")
    break

w = w[0]
x = range(-3,3,1)
y = (-b-(w[0]*x))/w[1]
plt.plot(x, y)



print(w[0])
print(w[1])
print(b)









plt.show()
