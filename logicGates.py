import numpy as np

def andGate():
  return np.array([ [0,0,0],[0,1,0], [1,0,0], [1,1,1] ])

def orGate():
  return np.array([ [0,0,0],[0,1,1], [1,0,1], [1,1,1] ])


def nandGate():
  return np.array([ [0,0,1],[0,1,1], [1,0,1], [1,1,0] ])

def norGate():
  return np.array([ [0,0,1],[0,1,0], [1,0,0], [1,1,0] ])

def all1Gate():
  return np.array([ [0,0,1],[0,1,1], [1,0,1], [1,1,1] ])

def all0Gate():
  return np.array([ [0,0,0],[0,1,0], [1,0,0], [1,1,0] ])



def getGate(gateString): 
  if gateString == "and":
    out = andGate()
  elif gateString == "or":
    out = orGate()
  elif gateString == "nand":
    out = nandGate()
  elif gateString == "nor":
    out = norGate()
  elif gateString == "all1":
    out = all1Gate()
  elif gateString == "all0":
    out = all0Gate()
  return out

