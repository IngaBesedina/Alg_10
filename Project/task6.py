#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import heapq
import numpy as np


def sort_sums(list1, list2):
    sum_el = []

    list1.sort()
    list2.sort()

    heap = [(list1[0] + list2[0], 0, 0)]
    pushed = {(0, 0)}
    for _ in range(len(list1) * len(list2)):
        s, i, j = heapq.heappop(heap)
        pushed.discard((i, j))
        sum_el.append(s)

        if i + 1 < len(list1) and (i + 1, j) not in pushed:
            heapq.heappush(heap, (list1[i + 1] + list2[j], i + 1, j))
            pushed.add((i + 1, j))

        if j + 1 < len(list2) and (i, j + 1) not in pushed:
            heapq.heappush(heap, (list1[i] + list2[j + 1], i, j + 1))
            pushed.add((i, j + 1))

    return sum_el


def main():
    list1 = np.array(np.random.randint(-100, 100, 5))
    list2 = np.array(np.random.randint(-100, 100, 5))
    print(sort_sums(list1, list2))


if __name__ == '__main__':
    main()
