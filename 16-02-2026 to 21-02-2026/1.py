import sys


def read_ints():
	return list(map(int, sys.stdin.readline().strip().split()))


def main():
	data = sys.stdin.read().strip().split()
	if not data:
		return
	it = iter(data)
	try:
		n = int(next(it))
		m = int(next(it))
		q = int(next(it))
	except StopIteration:
		return

	a = [[0]*m for _ in range(n)]
	for i in range(n):
		for j in range(m):
			try:
				a[i][j] = int(next(it))
			except StopIteration:
				a[i][j] = 0

	queries = []
	for _ in range(q):
		try:
			r1 = int(next(it)); c1 = int(next(it)); r2 = int(next(it)); c2 = int(next(it))
		except StopIteration:
			break
		queries.append((r1, c1, r2, c2))

	# build prefix sum (1-based padding)
	ps = [[0]*(m+1) for _ in range(n+1)]
	for i in range(1, n+1):
		row_sum = 0
		for j in range(1, m+1):
			row_sum += a[i-1][j-1]
			ps[i][j] = ps[i-1][j] + row_sum

	out_lines = []
	for r1, c1, r2, c2 in queries:
		# assume input indices are 0-based inclusive
		r1p, c1p, r2p, c2p = r1, c1, r2, c2
		s = ps[r2p+1][c2p+1] - ps[r1p][c2p+1] - ps[r2p+1][c1p] + ps[r1p][c1p]
		out_lines.append(str(s))

	sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
	main()

