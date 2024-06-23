import math


def is_number(n):
    try:
        float(n)
    except:
        return False

    return True


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    if x <= 0:
        return 0
    else:
        return x


def elu(x):
    alpha = 0.01
    if x <= 0:
        return alpha * (math.exp(x) - 1)
    else:
        return x


def activate_function(function, x):
    if function in [sigmoid, relu, elu]:
        if is_number(x):
            return function(x)
        else:
            return 'x must be a number'
    else:
        return 'please enter sigmoid or relu or elu'


activate_function(sigmoid, 1.5)
