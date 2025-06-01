"""
Task#4:

A fitness coach is analyzing heart rate data collected from four different athletes over four workout sessions. 
The data is stored in a 4x4 NumPy array where each row represents a workout session and each column 
represents an athlete.

[[85, 88, 90, 87],

[82, 85, 88, 84],

[89, 83, 85, 82],

[78, 80, 83, 79]]

(a) If the coach wants to split the data horizontally to analyze heart rates across two groups of workout sessions, which NumPy function should they use, and what would the resulting arrays look like? Write the code as well.

(b) To analyze data athlete-wise by splitting the matrix vertically, which NumPy function should be used? What would the resulting arrays represent? Write the code as well.

"""
import numpy as np
heart_rate=np.array([[85,88,90,87],[82,85,88,84],[89,83,85,82],[78,80,83,79]])
horiz=np.hsplit(heart_rate,2)
print("Horizontal Split",horiz)
vert=np.vsplit(heart_rate,4)
print(vert)