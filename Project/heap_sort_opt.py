#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import timeit as ti
import heapq
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def min_heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)

    return [heapq.heappop(h) for i in range(len(h))]


def n_log_n(x, a, b):
    return a * x * np.log(x) + b


def timer(num):
    y = []
    repeat = 30
    for n in range(10, num + 1, 10):
        random_list = np.array(np.random.randint(-100, 100, n))
        y.append(ti.timeit(lambda: min_heap_sort(random_list), number=repeat) / repeat)
    return y


def create_graphs(x, y):
    popt, pcov = curve_fit(n_log_n, x, y)
    a_opt, b_opt = popt

    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = n_log_n(x_fit, a_opt, b_opt)

    plt.scatter(x, y, s=5, color="b")
    plt.plot(x_fit, y_fit, color="r")
    plt.xlabel("Размер массива")
    plt.ylabel("Время работы функции")
    plt.title("Использование минимальной кучи")
    plt.show()


def main():
    num = 1000
    x = np.array(range(10, num + 1, 10))
    y = timer(num)

    create_graphs(x, y)


if __name__ == '__main__':
    main()
