import numpy as np
import matplotlib.pyplot as plt
from random import seed, randrange
import math

# Правило формирования конвертов (см readme.txt):
# Ведущий выбирает случайное число S, распределенное по какому-то закону P(x). Это - сумма X и Y, при этому X и Y
# распределяются по конвертам случайно.
# то есть, P(X=2/3S) = 1/2 и P(X=1/3S) = 1/2


# Рассмотрим пример с экспоненциальным распределением F(x) = 1 - e^(-lx)


def CumFunc(x, lam):
    if x >= 0:
        return 1 - pow(math.e, (-lam * x))


# обратная функция -1/l * ln(1-x), вместо x подставлять выборку из равномерного распределения
def ReverseFunc(x, lam):
    if x >= 0:
        return -1/lam*math.log(1-x)


# плотность распределения:
def Density(x, lam):
    if x >= 0:
        return lam * pow(math.e, (-lam * x))

# график

# x = np.arange(0, 6, 0.05)
# plt.plot(x, [Density(i, 0.5) for i in x])
# plt.plot(x, [Density(i, 1) for i in x])
# plt.plot(x, [Density(i, 1.5) for i in x])
# plt.show()

# Проведите численное моделирование игры:
# сгенерируйте выборку значений суммы в двух конвертах,

# сначала для этого сгенерируем выборку из стандартного непрерывного равномерного распределения
iterations = 10000
uni_sample = np.random.sample(iterations)
# затем создадим выборку из экспоненциального распределения
exp_sample_hard_way = np.array([ReverseFunc(x, 2) for x in uni_sample])

# короткий путь: известные распределения уже есть в numpy
# exp_sample = np.random.exponential(0.5, iterations)

fig, ax = plt.subplots(figsize=(8, 4))
n_bins = 50
n, bins, patches = ax.hist(exp_sample_hard_way, n_bins, normed=1, histtype='step',
                           cumulative=True, label='Empirical')

x = np.arange(0, 5, 0.05)
ax.plot(x, [CumFunc(i, 2) for i in x], 'k--', linewidth=1.5, label='Theoretical')

ax.grid(True)
ax.legend(loc='right')
ax.set_title('Cumulative step histograms')
ax.set_xlabel('Sample')
ax.set_ylabel('Likelihood of occurrence')

plt.show()

# разложите случайным образом суммы по конвертам.
# Отметьте реализации игры, в которых вам достался конверт с наибольшей суммой,
# для всех реализаций посчитайте величину выигрыша при обмене конвертами.
# Сгруппировав игры по близким значениям сумм в конверте первого игрока, посчитайте долю реализаций
# с большей суммой в конверте первого игрока и средний выигрыш первого игрока при обмене конвертами
# внутри каждой группы. Постройте графики оценки условной вероятности получить конверт с максимальной суммой
# и условного математического ожидания выигрыша при обмене конвертами, как функции от числа денег в конверте игрока X.







#
# seed()
# S = []
# for i in range(iterations):
#     S.append(ReverseFunc(randrange(0,1)))
# # как построить график? гистограмма по интервалам?
# # График для экспоненты (допустим)
#
# x = np.arange(0, 1000, 1)
# plt.plot(x, [IntFunc(i) for i in x])

# Итерация 2:
# Сумма случайно делится на X и Y, посчитать, сколько раз выиграла стратегия менять конверт

