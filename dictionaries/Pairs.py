# TODO: Optimize to use binary search on min/max bound
def count_differences(arr, difference):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) == difference:
                count += 1
    return count


if __name__ == '__main__':
    arr = [1, 5, 3, 4, 2]
    difference = 2
    print(count_differences(arr, difference))
