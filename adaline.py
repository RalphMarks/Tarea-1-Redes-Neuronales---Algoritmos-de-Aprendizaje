import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import math
import random

from io import StringIO

'''
La meta de este programa es programar
la regla de aprendizaje del perceptron
y la regla delta
'''

# FUNCTIONS
def  createplot(xdata, ydata):
  fig = plt.figure()
  axes = plt.gca()
  axes.set_xlim(-3, +3)
  axes.set_ylim(-3, +3)
  line, = axes.plot(xdata, ydata, 'r-')
  plt.grid(True)
  fig.suptitle('Adaline')
  firstClass = mpatches.Patch(color='red', label='Clase 1')
  secondClass = mpatches.Patch(color='blue', label='Clase 2')
  plt.legend(handles=[firstClass, secondClass])

  return line, plt

def getInputVector(dataFile):
  p = np.genfromtxt(f'data/{dataFile}.txt', dtype='int')
  return p

def graphDataPoints(p, plt):
  for row in p:
    if row[2] == 1:
      plt.plot(row[0], row[1], 'ro')
    else:
      plt.plot(row[0], row[1], 'bo')

def drawDecisionBoundary(line, plt, w):
  w = w[0]
  xdata = range(-3,3,1)
  ydata = []
  for x in xdata:
    ydata.append((-w[2]-(w[0]*x))/w[1])
  line.set_xdata(xdata)
  line.set_ydata(ydata)
  plt.draw()
  plt.pause(0.001)

def isClassified(errors,minError):
  result = True
  for error in errors:
    if abs(error) > minError:
      result = False
  return result

def drawErrors(errors):
  plt.figure()
  axese = plt.gca()
  axese.set_xlim(0, len(errors))
  axese.set_ylim(0, 10)
  axese.plot(range(len(errors)), errors, 'r-')

def hardlim(x):
  if x >= 0:
    return 1
  else:
    return 0

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

# EXECUTION
xdata = []
ydata = []


line, plt = createplot(xdata, ydata)


dataFile = input('Escoge datos de entrada: ')
eras = int(input('cuantas epocas: '))
minError = float(input('error minimo: '))

inputs = getInputVector(dataFile)

graphDataPoints(inputs, plt)

#init data
w = np.array([[np.round(random.random(), 2), np.round(random.random(), 2), np.round(random.random(), 2)]])
learningRate = 0.01
errors = []

print(f'w: {w}')

for z in range(eras):
  errorHelper = []
  for row in inputs:
    p = np.append(np.array([row[:2]]), [1]).T #creating column vector
    t = row[2] # target
    a = sigmoid(np.dot(w, p))
    #print(a)
    e = 20*(t - a)
    print(e)
    w = w + (2*learningRate*e*p).T
    w = w.round(10)
    #print(w)
    errorHelper.append(e)
    errors.append(e)
    drawDecisionBoundary(line, plt, w)
    
  if isClassified(errorHelper, minError):
    print("ya clasifico")
    break

print(f'errors: {len(errors)}')
drawErrors(errors)
plt.show()