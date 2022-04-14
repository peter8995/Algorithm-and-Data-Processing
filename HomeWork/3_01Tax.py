import math
import matplotlib.pyplot as plt

def revenue(tax):
    return (100 * (math.log(tax+1) - (tax - 0.2) ** 2 + 0.04))

current_rate = 0.7

xs = [x / 1000 for x in range(1001)]
ys = [revenue(x) for x in xs]
plt.plot(xs, ys)
plt.plot(current_rate, revenue(current_rate,), 'ro')
plt.title('Tax Rates and Revenue')
plt.xlabel('Tax Rate')
plt.ylabel('Revenus')
plt.show()