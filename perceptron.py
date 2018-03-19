import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.animation as animation

from io import StringIO

'''
La meta de este programa es programar
la regla de aprendizaje del perceptron
y la regla delta
'''

# FUNCTIONS
def  createplot():
  fig = plt.figure()
  plt.axis([-3, 3, -3, 3])
  plt.grid(True)
  fig.suptitle('Perceptron')
  firstClass = mpatches.Patch(color='red', label='Clase 1')
  secondClass = mpatches.Patch(color='blue', label='Clase 2')
  plt.legend(handles=[firstClass, secondClass])

  return plt

def getInputVector(dataFile):
  p = np.genfromtxt(f'data/{dataFile}.txt', dtype='int')
  return p

def graphDataPoint(p, plt):
  for row in p:
    if row[2] == 1:
      plt.plot(row[0], row[1], 'ro')
    else:
      plt.plot(row[0], row[1], 'bo')

def drawDecisionBoundary(w, plt):
  pass
# EXECUTION

plt = createplot()


dataFile = input('Escoge datos de entrada: ')

p = getInputVector(dataFile)

graphDataPoint(p, plt)






plt.show()
