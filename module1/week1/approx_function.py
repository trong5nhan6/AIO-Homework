def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def approx_sin(x, n):
    sum_x = 0
    for i in range(n):
        x_i = (-1)**(i) * (x)**(2*i + 1) / factorial(2*i + 1)
        sum_x += x_i
    return sum_x


def approx_cos(x, n):
    sum_x = 0
    for i in range(n):
        x_i = (-1)**(i) * (x)**(2*i) / factorial(2*i)
        sum_x += x_i
    return sum_x


def approx_sinh(x, n):
    sum_x = 0
    for i in range(n):
        x_i = (x)**(2*i + 1) / factorial(2*i + 1)
        sum_x += x_i
    return sum_x


def approx_cosh(x, n):
    sum_x = 0
    for i in range(n):
        x_i = (x)**(2*i) / factorial(2*i)
        sum_x += x_i
    return sum_x


print(approx_cosh(x=3.14, n=10))
