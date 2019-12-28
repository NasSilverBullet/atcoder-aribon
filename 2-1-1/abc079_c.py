s = input()
nbits = 1 << len(s) - 1
for bit in range(nbits):
    for i in range(len(s)):
        if i == 0:
            anss = s[0]
            ans = int(s[0])
            continue

        if bit & 1 << i - 1:
            anss += "+" + s[i]
            ans += int(s[i])
        else:
            anss += "-" + s[i]
            ans -= int(s[i])
    if ans == 7:
        print(anss + "=7")
        exit(0)
