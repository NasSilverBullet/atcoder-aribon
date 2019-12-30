# -*- coding: utf-8 -*-
# 再帰関数
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


print(fact(10))

# フィボナッチ数列
def fib(n):
    if n <= 1:
        return n

    return fib(n - 2) + fib(n - 1)


print(fib(10))

memo = [0 for _ in range(1000)]

# メモ化
def fib_memo(n):
    if n <= 1:
        return n

    if memo[n] != 0:
        return memo[n]

    memo[n] = fib_memo(n - 2) + fib_memo(n - 1)
    return memo[n]


print(fib_memo(10))

# スタック
def stack():
    s = []
    s.append(1)
    s.append(2)
    s.append(3)
    print(s[-1])
    s.pop()
    print(s[-1])
    s.pop()
    print(s[-1])


stack()

from collections import deque


# キュー
def queue():
    q = deque([])
    q.append(1)
    q.append(2)
    q.append(3)
    print(q[0])
    q.popleft()
    print(q[0])
    q.popleft()
    print(q[0])
    q.popleft()


queue()
