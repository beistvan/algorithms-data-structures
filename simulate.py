from collections import deque

def simulate(buffer_size, packets):
    buffer = deque()
    result = []
    current_time = 0

    for arrival, duration in packets:
        while buffer and buffer[0] <= arrival:
            buffer.popleft()

        if len(buffer) >= buffer_size:
            result.append(-1)
        else:
            start_time = max(buffer[-1] if buffer else 0, arrival)
            finish_time = start_time + duration
            buffer.append(finish_time)
            result.append(start_time)

    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    s = int(data[0])
    n = int(data[1])

    packets = []
    for i in range(n):
        arrival = int(data[2 + 2*i])
        duration = int(data[2 + 2*i + 1])
        packets.append((arrival, duration))

    output = simulate(s, packets)
    for line in output:
        print(line)
