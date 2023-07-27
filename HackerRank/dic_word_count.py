# You are given  words. Some words may repeat. For each word, output its number of occurrences. 
# The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
from collections import defaultdict

n = int(input())
words = defaultdict(int)
for _ in range(n):
    w = input()
    words[w] += 1
print(len(words))
print(*words.values())
