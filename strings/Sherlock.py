from collections import Counter


def has_valid_freqs(counts):
    """
    Return True if all letters have the same frequency,
    or if deleting a single occurrence of a character
    makes all remaining letters have the same frequency.

    :param counts: A dictionary of frequency to number of letters having that frequency
    :return: bool
    """
    if len(counts) > 2:
        return False
    elif len(counts) == 1:
        return True
    elif 1 in counts and counts[1] == 1:
        return True
    else:
        fst, snd = counts
        if counts[fst] == 1:
            return fst - snd == 1
        elif counts[snd] == 1:
            return snd - fst == 1
        else:
            return False


def is_valid(s):
    c = Counter(s)
    freqs = Counter(c.values())
    return 'YES' if has_valid_freqs(freqs) else 'NO'


if __name__ == '__main__':
    positives = [
        {1: 1},
        {1: 2},
        {2: 3},
        {3: 2, 1: 1},
        {1: 1, 3: 2},
        {2: 2, 3: 1},
        {3: 1, 2: 2}
    ]

    for d in positives:
        assert has_valid_freqs(d)

    negatives = [
        {2: 2, 3: 2},
        {2: 1, 4: 1},
        {4: 1, 2: 1},
        {1: 2, 3: 2},
        {1: 1, 2: 1, 3: 1}
    ]

    for d in negatives:
        assert not has_valid_freqs(d)

    print(is_valid('caabbcc'))

