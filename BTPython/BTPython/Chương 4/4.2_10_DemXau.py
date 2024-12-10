rep = int(input())
for i in range(1, rep + 1):
    previous_char = None
    s = input()
    count = 1
    kq = ""
    for current_char in s:
        if current_char == previous_char:
            count += 1
        else:
            if previous_char is not None:
                kq += f"{previous_char}{count}"
                count = 1
        previous_char = current_char

    kq += f"{previous_char}{count}"
    print(kq)