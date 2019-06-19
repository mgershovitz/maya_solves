from heapq import heappop, heappush

def sort_approximate(arr, k):
    if k == 0:
        return arr
    sorted_arr = list()
    heap = []

    for i in range(0, k):
        heappush(heap, arr[i])

    for i in range(k, len(arr)):
        sorted_arr.append(heappop(heap))
        heappush(heap,arr[i])

    for i in range(0, k):
        sorted_arr.append(heappop(heap))

    return sorted_arr

def run_tests():
    examples = [
        (3,[3, 1, 4, 2, 7, 6, 5]),
        (0,[1,2]),
        (7, [3, 1, 4, 2, 7, 6, 5]),
        (7, [35, 70, 61, 24, 53, 40, 1, 14, 30, 29, 100, 99, 36]),
    ]
    for (k,arr) in examples:
        print("Original array - ")
        print(arr)
        sorted_array = sort_approximate(arr, k)
        print("Array after sorting - ")
        print(sorted_array)


if __name__ == '__main__':
    run_tests()
