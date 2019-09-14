
def counting_valleys(s: str) -> int:
    valley_count = 0
    level = 0
    in_valley = False

    for ch in s:
        if ch == 'D':
            if level == 0:
                in_valley = True
            level -= 1
        else:
            level += 1

        if level == 0 and in_valley:
            in_valley = False
            valley_count += 1

    return valley_count


if __name__ == '__main__':
    print(counting_valleys('UDDDUDUU'))
