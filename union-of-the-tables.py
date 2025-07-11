import sys

class DSU:
    def __init__(self, size, rows):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.rows = rows[:]
        self.max_row_count = max(rows)

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, dest, src):
        real_dest = self.find(dest)
        real_src = self.find(src)
        if real_dest == real_src:
            return self.max_row_count

        if self.rank[real_dest] < self.rank[real_src]:
            real_dest, real_src = real_src, real_dest

        self.parent[real_src] = real_dest
        self.rows[real_dest] += self.rows[real_src]
        self.rows[real_src] = 0
        if self.rank[real_dest] == self.rank[real_src]:
            self.rank[real_dest] += 1

        self.max_row_count = max(self.max_row_count, self.rows[real_dest])
        return self.max_row_count


def main():
    n, m = map(int, sys.stdin.readline().split())
    rows = list(map(int, sys.stdin.readline().split()))
    dsu = DSU(n, rows)

    for _ in range(m):
        dest, src = map(int, sys.stdin.readline().split())
        print(dsu.union(dest - 1, src - 1))

if __name__ == "__main__":
    main()
