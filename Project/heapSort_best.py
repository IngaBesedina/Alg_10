#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import timeit as ti
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def heapify(sort_list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and sort_list[i] < sort_list[left]:
        largest = left

    if right < n and sort_list[largest] < sort_list[right]:
        largest = right

    if largest != i:
        sort_list[i], sort_list[largest] = sort_list[largest], sort_list[i]
        heapify(sort_list, n, largest)


def heap_sort(sort_list):
    n = len(sort_list)

    for i in range(n // 2 - 1, -1, -1):
        heapify(sort_list, n, i)

    for i in range(n - 1, 0, -1):
        sort_list[i], sort_list[0] = sort_list[0], sort_list[i]
        heapify(sort_list, i, 0)


def n_log_n(x, a, b):
    return a * x * np.log(x) + b


def timer(num):
    y = []
    repeat = 30
    for n in range(10, num + 1, 10):
        sort_list = np.array(np.random.randint(-100, 100, n))
        sort_list.sort()
        y.append(ti.timeit(lambda: heap_sort(sort_list), number=repeat) / repeat)
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
    plt.title("Лучший случай")
    plt.show()


def main():
    num = 1000
    x = np.array(range(10, num + 1, 10))
    y = timer(num)

    create_graphs(x, y)


if __name__ == '__main__':
    main()
