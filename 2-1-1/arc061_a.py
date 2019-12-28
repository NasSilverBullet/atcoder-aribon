# bit 全探索
s = input()
nbits = 1 << (len(s) - 1)
ans = 0
for bit in range(nbits):
    tmp = []
    for i in range(len(s) - 1):
        if bit & (1 << i):
            tmp.append(i)

    curr = 0
    for x in tmp:
        ans += int(s[curr : x + 1])
        curr = x + 1
    ans += int(s[curr:])

print(ans)
