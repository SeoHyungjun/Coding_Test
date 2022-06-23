import sys

N = int(sys.stdin.readline())
word_set = set()

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    in_word_set = False
    for i in range(len(word)):
        cur_word = word[i:] + word[:i]
        if cur_word in word_set:
            in_word_set = True
            break

    if not in_word_set:
        word_set.add(word)

print(len(word_set))