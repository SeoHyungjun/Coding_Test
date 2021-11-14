import sys

class Trie:
    def __init__(self):
        self.children = {}

    def add(self, foods):
        cur = self.children

        for food in foods:
            if food not in cur:
                cur[food] = Trie()
            cur = cur[food].children

    def search(self, level):
        for ch_key in sorted(self.children.keys()):
            print('--'*level, ch_key, sep = '')
            self.children[ch_key].search(level + 1)

N = int(sys.stdin.readline())
root = Trie()
for _ in range(N):
    foods = sys.stdin.readline().rstrip().split()[1:]
    root.add(foods)

root.search(0)