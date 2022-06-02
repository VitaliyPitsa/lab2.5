#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    arr = tuple(map(int, input().split()))
    print("кортеж:", arr)

    for i, x in enumerate(arr):
        e1 = arr[i]
        e2 = arr[i + 1]
        e3 = arr[i + 2]
        if e1 < e2 > e3:
            print("индексы элементов кортежа:", i, i + 1, i + 2, " их значения:", e1, e2, e3)
            break