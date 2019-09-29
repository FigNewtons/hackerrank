from collections import defaultdict


def count_triples(arr, ratio):
    count = 0
    pairs = defaultdict(int)
    triples = defaultdict(int)
    for num in arr:
        count += triples[num]
        triples[num * ratio] += pairs[num]
        pairs[num * ratio] += 1
    return count


if __name__ == '__main__':
    arr = [1, 3, 1, 9, 3, 9, 27, 81, 1, 9, 27, 27, 3, 3, 9, 81, 27, 27, 1, 1]
    ratio = 3
    print(count_triples(arr, ratio))
