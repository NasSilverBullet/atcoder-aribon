def dfs(i, s, ex):
    if i == 4:
        if s == 7:
            return ex + "=7"
        else:
            return ""

    if i == 0:
        return dfs(i + 1, int(S[i]), S[i])

    return dfs(i + 1, s + int(S[i]), ex + "+" + S[i]) or dfs(
        i + 1, s - int(S[i]), ex + "-" + S[i]
    )


S = input()
print(dfs(0, 0, ""))
