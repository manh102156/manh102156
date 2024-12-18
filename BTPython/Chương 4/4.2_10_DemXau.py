n, q = map(int, input().split())
s = input()

freq = [[0] * (n + 1) for _ in range(26)]

for i in range(1, n + 1):
    char_idx = ord(s[i - 1]) - ord('a')
    for j in range(26):
        freq[j][i] = freq[j][i - 1]
    freq[char_idx][i] += 1

for _ in range(q):
    l, r, c = input().split()
    l, r = int(l), int(r)
    char_idx = ord(c) - ord('a')
    result = freq[char_idx][r] - freq[char_idx][l - 1]
    print(result)
