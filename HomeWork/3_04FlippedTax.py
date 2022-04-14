import math
import matplotlib.pyplot as plt

def revenue_flipped(tax):
    return(0 - revenue(tax))

def revenue(tax):
    return (100 * (math.log(tax+1) - (tax - 0.2) ** 2 + 0.04))

xs = [x / 1000 for x in range(1001)]
ys = [revenue_flipped(x) for x in xs]
plt.plot(xs, ys)
plt.title('The Tax/Revenue Curve - Flipped')
plt.xlabel('Current Tax Rate')
plt.ylabel('Revenue - Flipped')
plt.show()