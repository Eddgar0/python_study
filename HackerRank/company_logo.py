
import math
import os
import random
import re
import sys
from collections import OrderedDict, Counter


if __name__ == '__main__':
    s = input()
    words = Counter(s)
    words = OrderedDict(sorted(words.items(), key=lambda t: t[0]))
    words = OrderedDict(sorted(words.items(), reverse=True, key=lambda t: t[1]))
    top3 = list(words.items())
    for word, count in top3[:3]:
        print(word, count)
