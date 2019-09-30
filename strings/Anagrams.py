from collections import Counter


def anagram(a, b):
    deletions = 0

    if len(a) == min(len(a), len(b)):
        s = a
        c = Counter(b)
    else:
        s = b
        c = Counter(a)

    for ch in s:
        if ch in c:
            c[ch] -= 1
            if c[ch] == 0:
                del c[ch]
        else:
            deletions += 1

    deletions += sum(c.values())
    return deletions


if __name__ == '__main__':
    print(anagram('cde', 'abc'))

