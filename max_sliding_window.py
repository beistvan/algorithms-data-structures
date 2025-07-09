from collections import deque

def max_sliding_window(arr, k):
    dq = deque()
    result = []

    for i in range(len(arr)):
        if dq and dq[0] == i - k:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(arr[dq[0]])

    return result

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())

    output = max_sliding_window(arr, k)
    print(" ".join(map(str, output)))
