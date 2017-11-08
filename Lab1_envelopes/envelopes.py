import numpy as np
import matplotlib.pyplot as plt
# Допустим, сумма x распределена по логнормальному закону
#
# #x = 100 * np.random.lognormal(0,1,100)
# x = 1000 * np.random.f(15,20,100)
# # plt.plot(x, [alpha(i, 1.7, 0.7) for i in x])
# # plt.show()
# print(x)

# Правило формирования конвертов:
# Ведущий выбирает случайное число X, распределенное по какому-то закону P(x). Это - большая сумма, меньшая составит
# X/2.