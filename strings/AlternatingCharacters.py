def count_deletes(s):
    deletes = 0
    ch = s[0]
    for i in range(1, len(s)):
        if ch == s[i]:
            deletes += 1
        else:
            ch = s[i]
    return deletes


if __name__ == '__main__':
    print(count_deletes('AAABBB'))
