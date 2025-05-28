n = int(input())
count = 0

for _ in range(n):
    word = input()
    seen = set()
    prev = ''
    flag = True

    for ch in word:
        if ch != prev:
            if ch in seen:
                flag = False
                break
            seen.add(ch)
        prev = ch

    if flag:
        count += 1

print(count)