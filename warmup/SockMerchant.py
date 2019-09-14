from typing import List


def count_pairs(socks: List[int]) -> int:
    pair_count = 0
    unpaired = set()
    for sock in socks:
        if sock in unpaired:
            pair_count += 1
            unpaired.remove(sock)
        else:
            unpaired.add(sock)

    return pair_count


if __name__ == '__main__':
    print(count_pairs([10, 20, 20, 10, 10, 30, 50, 10, 20]))
