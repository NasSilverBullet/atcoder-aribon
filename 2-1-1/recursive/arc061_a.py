from functools import reduce
from operator import add


def dfs(i, a):
    if i == N:
        return reduce(add, map(int, a.split("+")))

    if i == 0:
        return dfs(i + 1, S[i])

    return dfs(i + 1, a + S[i]) + dfs(i + 1, a + "+" + S[i])


S = input()
N = len(S)
print(dfs(0, ""))
