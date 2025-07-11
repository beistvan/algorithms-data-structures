import heapq
import sys

def parallel_processing(n, m, jobs):
    result = []
    heap = [(0, i) for i in range(n)]
    heapq.heapify(heap)

    for job in jobs:
        time_free, proc_id = heapq.heappop(heap)
        result.append((proc_id, time_free))
        heapq.heappush(heap, (time_free + job, proc_id))

    return result

def main():
    n, m = map(int, sys.stdin.readline().split())
    jobs = list(map(int, sys.stdin.readline().split()))

    output = parallel_processing(n, m, jobs)
    for proc_id, start_time in output:
        print(proc_id, start_time)

if __name__ == "__main__":
    main()
