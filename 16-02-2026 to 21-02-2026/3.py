import sys
import heapq


def parse_input_tokens(s: str):
    # replace common non-numeric separators and split
    for ch in '[],':
        s = s.replace(ch, ' ')
    return s.split()


def main():
    data = sys.stdin.read()
    if not data.strip():
        return
    toks = parse_input_tokens(data)
    if not toks:
        return

    # If first token is an integer count matching remaining tokens, use it.
    arr = []
    try:
        first = int(toks[0])
        if len(toks) - 1 == first:
            # format: n followed by n numbers
            for x in toks[1:]:
                arr.append(float(x))
        else:
            # otherwise treat all tokens as array values
            for x in toks:
                arr.append(float(x))
    except Exception:
        for x in toks:
            try:
                arr.append(float(x))
            except Exception:
                pass

    if not arr:
        print(0)
        return

    total = sum(arr)
    target = total / 2.0
    # max-heap via negatives
    heap = [-x for x in arr]
    heapq.heapify(heap)

    ops = 0
    curr = total
    while curr > target:
        largest = -heapq.heappop(heap)
        halved = largest / 2.0
        curr -= (largest - halved)
        heapq.heappush(heap, -halved)
        ops += 1

    print(ops)


if __name__ == '__main__':
    main()
