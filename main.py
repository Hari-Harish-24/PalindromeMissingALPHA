word = input().strip()
wordr = word[::-1]
for i in range(len(word)):
    if word[i]==wordr[i]:
        continue
    else:
        if word[i+1]==wordr[i]:
            print(word[i])
        else:
            print(wordr[i])
        break