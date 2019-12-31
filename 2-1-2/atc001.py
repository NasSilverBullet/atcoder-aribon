def dfs(city, checked, H, W):
    start = []

    for i, hs in enumerate(c):
        for j, p in enumerate(hs):
            if p == "s":
                start = [i, j]
                break

    stack = []
    stack.append(start)

    while stack:
        h, w = stack.pop()
        if city[h][w] == "g":
            return "Yes"

        for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if not (0 <= h + x < H) or not (0 <= w + y < W):
                continue

            if city[h + x][w + y] == "#":
                continue

            if checked[h + x][w + y]:
                continue

            checked[h + x][w + y] = True

            stack.append([h + x, w + y])

    return "No"


H, W = map(int, input().split())
c = [input() for _ in range(H)]
checked = [[False] * W for _ in range(H)]


print(dfs(c, checked, H, W))
