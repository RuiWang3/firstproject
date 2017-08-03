import numpy as np 
import matplotlib.pyplot as plt
plt = np.read_csv("Data/py.csv")
lotArea=plt[['lotArea']]
Print(plt['lotArea'].describe())