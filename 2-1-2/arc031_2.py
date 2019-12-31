import copy


def search(a, tx, ty):
    s = 0
    stack = []
    searched = [[False for _ in range(10)] for _ in range(10)]
    stack.append([tx, ty])

    while stack:
        x, y = stack.pop()
        if not ((0 <= x < 10) and (0 <= y < 10)):
            continue

        if searched[x][y]:
            continue

        if a[x][y] != "o":
            continue

        s += 1
        searched[x][y] = True
        stack.append([x - 1, y])
        stack.append([x + 1, y])
        stack.append([x, y - 1])
        stack.append([x, y + 1])

    return s


A = [list(input()) for _ in range(10)]
land_cnt = 0

for i in range(10):
    for j in range(10):
        if A[i][j] == "o":
            land_cnt += 1
            continue

for i in range(10):
    for j in range(10):
        if A[i][j] == "o":
            continue

        copiedA = copy.deepcopy(A)
        copiedA[i][j] = "o"

        for ix in range(10):
            for jx in range(10):
                if copiedA[ix][jx] == "x":
                    continue

                if search(copiedA, ix, jx) == land_cnt + 1:
                    print("YES")
                    exit()

print("NO")
