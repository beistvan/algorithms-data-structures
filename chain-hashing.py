import sys

class HashTable:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, m):
        self.m = m
        self.table = [[] for _ in range(m)]

    def _hash(self, s):
        hash_val = 0
        for i in reversed(range(len(s))):
            hash_val = (hash_val * self._multiplier + ord(s[i])) % self._prime
        return hash_val % self.m

    def add(self, s):
        index = self._hash(s)
        if s not in self.table[index]:
            self.table[index].insert(0, s)

    def delete(self, s):
        index = self._hash(s)
        if s in self.table[index]:
            self.table[index].remove(s)

    def find(self, s):
        index = self._hash(s)
        return "yes" if s in self.table[index] else "no"

    def check(self, i):
        return " ".join(self.table[i])

def process_queries(queries):
    m = int(queries[0])
    n = int(queries[1])
    table = HashTable(m)
    output = []

    for query in queries[2:]:
        parts = query.strip().split()
        if parts[0] == 'add':
            table.add(parts[1])
        elif parts[0] == 'del':
            table.delete(parts[1])
        elif parts[0] == 'find':
            output.append(table.find(parts[1]))
        elif parts[0] == 'check':
            output.append(table.check(int(parts[1])))

    return output

def main():
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line)
    result = process_queries(input_lines)
    for line in result:
        print(line)

if __name__ == "__main__":
    main()
