from heapq import heappush, heappop, heapify
from collections import defaultdict
from itertools import groupby


def huffman_encoding(data):
    freq = defaultdict(int)
    for char in data:
        freq[char] += 1

    heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
    heapify(heap)

    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return dict(sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))


data = "aaaabbcrddd"
symbols = ''.join(k for k, g in groupby(data))
if len(symbols) > 1:
    encoded_data = huffman_encoding(data)
    print("Строка:", data)
    print("Коды символов:", encoded_data)
    print("Закодированная строка:", end=' ')
    for s in symbols:
        print(encoded_data[s], end='')
elif len(data) == 0:
    print("Пустая строка")
else:
    print(symbols, ': 0')
