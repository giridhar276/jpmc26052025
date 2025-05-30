# method1
## all the methods are imported to your programspace
import math 
print(math.log(1))
print(math.tan(1))

#method2  importing with alias name
import math as m
print(m.log(2))
print(m.cos(1))

import matplotlib.pyplot as plt     #pip install matplotlib
plt.plot([10,20],[20,30])
plt.show()

#method3 - importing required methods only
from math import log,tan,cos 
print(log(4))
print(tan(1))