import numpy as np
import matplotlib
import matplotlib.pyplot as plt

'''
La meta de este programa es programar
la regla de aprendizaje del perceptron
y la regla delta
'''
x = np.linspace(0, 2, 100)

fig = plt.figure()  # an empty figure with no axes
plt.axis([-4, 4, -4, 4])
plt.grid(True)
fig.suptitle('Perceptron')  # Add a title so we know which it is

plt.plot(0, 0, 'ro')
plt.plot(0, 1, 'ro')
plt.plot(1, 0, 'ro')
plt.plot(1, 1, 'ro')

plt.show()