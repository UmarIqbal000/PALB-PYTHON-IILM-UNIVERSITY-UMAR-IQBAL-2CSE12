import sys


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    nums = list(map(int, data))

    # If first value is n and matches remaining count, use it.
    if len(nums) >= 2 and nums[0] == len(nums) - 1:
        n = nums[0]
        arr = nums[1:]
    else:
        arr = nums
        n = len(arr)

    intervals = []
    for i, val in enumerate(arr):
        if val == -1:
            continue
        l = max(0, i - val)
        r = min(n - 1, i + val)
        intervals.append((l, r))

    if not intervals:
        print(-1)
        return

    intervals.sort(key=lambda x: (x[0], -x[1]))

    covered = 0
    i = 0
    res = 0
    L = len(intervals)

    while covered <= n - 1:
        best = -1
        while i < L and intervals[i][0] <= covered:
            if intervals[i][1] > best:
                best = intervals[i][1]
            i += 1
        if best < covered:
            print(-1)
            return
        res += 1
        covered = best + 1

    print(res)


if __name__ == '__main__':
    main()
