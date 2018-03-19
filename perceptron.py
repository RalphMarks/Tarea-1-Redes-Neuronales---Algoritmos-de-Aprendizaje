import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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
  fig.suptitle('Perceptron')
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

def drawDecisionBoundary(line, plt, w, b):
  w = w[0]
  xdata = range(-3,3,1)
  ydata = []
  for x in xdata:
    ydata.append((-b-(w[0]*x))/w[1])
  line.set_xdata(xdata)
  line.set_ydata(ydata)
  plt.draw()
  plt.pause(0.001)

def isClassified(errors):
  result = True
  for error in errors:
    if error != 0:
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
w = np.array([[random.random(), random.random()]])
b = random.random()
learningRate = 0.01
errors = []

print(f'w: {w}')
print(f'b: {b}')

for z in range(eras):
  errorHelper = []
  for row in inputs:
    p = np.array([row[:2]]).T #creating column vector
    t = row[2] # target
    #print(p)
    a = hardlim(np.dot(w,p) + b)
    e = t - a # error
    w = w + (learningRate*e*p).T
    b = b + e
    errorHelper.append(e)
    errors.append(e)
    drawDecisionBoundary(line, plt, w, b)
    
  if isClassified(errorHelper):
    print("ya clasifico")
    break

print(f'errors: {len(errors)}')
drawErrors(errors)
plt.show()