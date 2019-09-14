
def count_occurrences(string: str, letter: str, end: int) -> int:
    count = 0
    for i in range(end):
        if letter == string[i]:
            count += 1
    return count


def repeated_string(s: str, n: int) -> int:
    # remainder
    count = count_occurrences(s, 'a', n % len(s))

    # dividend
    times = n // len(s)
    count += 0 if times == 0 else times * count_occurrences(s, 'a', len(s))
    return count


if __name__ == '__main__':
    print(repeated_string('aba', 10))


