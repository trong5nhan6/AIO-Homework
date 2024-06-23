import random
import math


def mae(n):
    loss = 0
    for i in range(n):
        y = random.uniform(0, 10)
        y_hat = random.uniform(0, 10)
        loss += abs(y - y_hat)
    return loss / n


def mse(n):
    loss = 0
    for i in range(n):
        y = random.uniform(0, 10)
        y_hat = random.uniform(0, 10)
        loss += (y - y_hat)**2
    return loss / n


def rmse(n):
    loss = mse(n)
    return math.sqrt(loss)


def regresion_loss(function, n):
    if function in [mae, mse, rmse]:
        if isinstance(n, int):
            return f'loss name: {function} sample: {n} loss: {function(n)}'
        else:
            return 'number of samples must be an integer number'
    else:
        return 'please enter mae or mse or rmse'


print(regresion_loss(mse, 6))
