def run_length(s):
    result = []
    n = len(s)
    i = 0
    while i < n:
        count = 1
        while i + 1 < n and s[i] == s[i + 1]:
            count += 1
            i += 1
        result.append(s[i] + str(count))
        i += 1
    return "".join(result)

n = int(input())
for i in range(n):
    s = input()
    print(run_length(s))