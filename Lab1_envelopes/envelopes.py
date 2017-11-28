import numpy as np
import matplotlib.pyplot as plt
from random import seed, randrange, randint
import math

# Дан некий закон распределения для суммы S. В качестве примера использовано показательное распределение,
# но может быть и другое:
# F(x) = 1 - e^(-lx)
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

# Правило формирования конвертов (см readme.txt):
# Ведущий выбирает случайное число S, распределенное по какому-то закону P(x). Это - сумма X и Y, при этом X и Y
# распределяются по конвертам случайно.

# В общем случае искомое E[Y-X | X = a] = E[ Y | |X-a|<epsilon ] - X
# (4) E[ Y-X | |X-a|<epsilon ] = (X/2 + O(epsilon)) *
# Density(3/2*a)*3/2*epsilon * P(X=2/3S) / (6)   +
# +  (2X + O(epsilon)) * Density(3*a)*3*epsilon * P(X=1/3S) / (6)    -    X

# Вспомогательная формула: вероятность того, что в конверте определенное число денег a:
# (6) P(|X - a| < epsilon) = Density(3/2*a)*3/2*epsilon*P(X=2/3S) + Density(3*a)*3*epsilon*P(X=1/3S)

def p_X_has_certain_amount(amount, epsilon, p_X_is_2Y, p_Y_is_2X):
    return Density(3/2*amount)*3/2*epsilon*p_X_is_2Y + Density(3*amount)*3*epsilon*p_Y_is_2X

def expectable_win(a, X, epsilon, p_X_is_2Y, p_Y_is_2X):
    formula_6 = p_X_has_certain_amount(a, epsilon, p_X_is_2Y, p_Y_is_2X)
    return X/2 * Density(3/2*a)*3/2*epsilon * p_X_is_2Y / formula_6 + 2*X * Density(3*a)*3*epsilon * p_Y_is_2X / formula_6 - X

# Пусть правило распределения X и Y такое:
# P(X=2/3S) = 1/2 и P(X=1/3S) = 1/2 (могут быть и другие)
p_X_is_bigger = 0.5
p_X_is_smaller = 1 - p_X_is_bigger
eps = 0.005


# Проведите численное моделирование игры:
# сгенерируйте выборку значений суммы в двух конвертах,

# сначала для этого сгенерируем выборку из стандартного непрерывного равномерного распределения
my_lambda = 0.3
iterations = 10000
uni_sample = np.random.sample(iterations)
# затем создадим выборку из данного по условию распределения
exp_sample = np.array([ReverseFunc(x, my_lambda) for x in uni_sample])

# короткий путь: многие известные распределения уже есть в numpy
# exp_sample_easy_way = np.random.exponential(0.5, iterations)

# Визуальная проверка (на графике), что выборка близка к теоретическому распределению:

# fig1, ax = plt.subplots(figsize=(8, 4))
# n_bins = 50
# n, bins, patches = ax.hist(exp_sample, n_bins, normed=1, histtype='step',
#                            cumulative=True, label='Empirical')
#
# x = np.arange(0, 25, 0.05)
# ax.plot(x, [CumFunc(i, my_lambda) for i in x], 'k--', linewidth=1.5, label='Theoretical')
# ax.grid(True)
# ax.legend(loc='right')
# ax.set_title('Comparison of theoretical distr-n and sample')
# ax.set_xlabel('Sample')
# ax.set_ylabel('Likelihood of occurrence')
# plt.show()


exp_sample.sort()
# умножение исключительно для удобства, чтобы не иметь дела с очень маленькими числами
exp_sample = exp_sample * 1000
# раскладываем суммы по конвертам случайным образом.
n = int(iterations * p_X_is_bigger)
# массив флагов поможет случайно вывести суммы X и Y из выборки сумм
flags = np.concatenate((np.ones(n), np.zeros(iterations - n)))
np.random.shuffle(flags)

wins_if_change = 0
wins = np.empty(iterations)
envelopes = []
for i in range(iterations):
    X = 2/3*exp_sample[i] if flags[randint(0,iterations-1)] else 1/3*exp_sample[i]
    Y = exp_sample[i] - X
    envelopes.append((X,Y))
    # Отмечаем реализации игры, в которых игроку достался конверт с наибольшей суммой
    if X < Y:
        wins_if_change += 1
    # для всех реализаций считаем величину выигрыша при обмене конвертами, записываем выигрыш в список
    wins[i] = Y - X

print("Wins ratio is {}".format(wins_if_change/iterations))
mean = wins.mean
print("Mean of wins is {}".format(wins.mean()))

envelopes_sorted = sorted(envelopes, key=lambda x: x[0])

# пусть групп будет 50 или меньше
n_groups = 50
# "ширина" одной группы
delta = (envelopes_sorted[-1][0] - envelopes_sorted[0][0]) / n_groups
print("delta is {}".format(delta))
minX = envelopes_sorted[0][0]
ratios_of_groups = []
j = 0
sum_of_group = 0
count_in_group = 0
wins_in_group = 0
group_wins_list = []
Xs = []
for i in range(iterations):
    if envelopes_sorted[i][0] <= minX+(j+1)*delta and i != iterations-1:
        if envelopes_sorted[i][0] > envelopes_sorted[i][1]:
            wins_in_group += 1
        sum_of_group = sum_of_group + envelopes_sorted[i][1] - envelopes_sorted[i][0]
        count_in_group +=1
    else:
        j += 1
        if count_in_group != 0:
            ratios_of_groups.append(sum_of_group/count_in_group)
            group_wins_list.append(wins_in_group/count_in_group)
            Xs.append(minX+j*delta)
        sum_of_group = 0
        count_in_group = 0
        wins_in_group = 0


# x = np.array(envelopes_sorted)
# x2 = np.hsplit(x, 2)
# X_list = x2[0]


fig2, ax2 = plt.subplots(figsize=(8, 4))

ax2.plot(Xs, ratios_of_groups, linewidth=1.5, label="Expected win")
ax2.plot(Xs, group_wins_list, linewidth=0.5, label="Probability of win with current sum")
ax2.grid(True)
ax2.legend(loc='right')
ax2.set_title('Strategy to change envelope')
ax2.set_xlabel('Sum in the current envelope')
ax2.set_ylabel('Expected prize')

fig3, ax3 = plt.subplots(figsize=(8, 4))
ax3.plot(Xs, group_wins_list, linewidth=1.5, label="Probability of win with current sum")
ax3.grid(True)
ax3.legend(loc='right')
ax3.set_title('Strategy of sticking to the current envelope')
ax3.set_xlabel('Sum in the current envelope')
ax3.set_ylabel('Likelohood of win')

plt.show()


