import sys


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it)); m = int(next(it))
    except StopIteration:
        return

    a = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            try:
                a[i][j] = int(next(it))
            except StopIteration:
                a[i][j] = 0

    try:
        q = int(next(it))
    except StopIteration:
        q = 0

    queries = []
    for _ in range(q):
        try:
            r = int(next(it)); c = int(next(it))
        except StopIteration:
            break
        queries.append((r, c))

    INF = 10**18
    # allocate (n+2)x(m+2) padded arrays
    tl = [[INF]*(m+2) for _ in range(n+2)]
    tr = [[INF]*(m+2) for _ in range(n+2)]
    bl = [[INF]*(m+2) for _ in range(n+2)]
    br = [[INF]*(m+2) for _ in range(n+2)]

    # top-left: min over rectangle (1,1) to (i,j)
    for i in range(1, n+1):
        for j in range(1, m+1):
            tl[i][j] = min(a[i][j], tl[i-1][j], tl[i][j-1], tl[i-1][j-1])

    # top-right: min over rectangle (1,j) to (i,m)
    for i in range(1, n+1):
        for j in range(m, 0, -1):
            tr[i][j] = min(a[i][j], tr[i-1][j], tr[i][j+1], tr[i-1][j+1])

    # bottom-left: min over rectangle (i,1) to (n,j)
    for i in range(n, 0, -1):
        for j in range(1, m+1):
            bl[i][j] = min(a[i][j], bl[i+1][j], bl[i][j-1], bl[i+1][j-1])

    # bottom-right: min over rectangle (i,j) to (n,m)
    for i in range(n, 0, -1):
        for j in range(m, 0, -1):
            br[i][j] = min(a[i][j], br[i+1][j], br[i][j+1], br[i+1][j+1])

    out = []
    for r, c in queries:
        s = 0
        # top-left
        if r > 1 and c > 1:
            v = tl[r-1][c-1]
            if v != INF:
                s += v
        # top-right
        if r > 1 and c < m:
            v = tr[r-1][c+1]
            if v != INF:
                s += v
        # bottom-left
        if r < n and c > 1:
            v = bl[r+1][c-1]
            if v != INF:
                s += v
        # bottom-right
        if r < n and c < m:
            v = br[r+1][c+1]
            if v != INF:
                s += v

        out.append(str(s))

    sys.stdout.write("\n".join(out))


if __name__ == '__main__':
    main()
