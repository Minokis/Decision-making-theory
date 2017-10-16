# отключим лишние предупреждения Anaconda
import warnings
warnings.filterwarnings('ignore')

import numpy as np
from math import pi, atan
import matplotlib.pyplot as plt


def alpha(x, m, f):
    return pi/2 - atan(x/m) - atan((m-f)/x)
# задаем иксы с некоторым мелким шагом
x = np.arange(0, 6, 0.05)
plt.plot(x, [alpha(i, 1.7, 0.7) for i in x])
plt.show()