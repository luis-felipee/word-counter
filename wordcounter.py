import pprint
from text import text

counts = dict()
text2 = text.split()

for name in text2:
    counts[name] = counts.get(name, 0) + 1
pprint.pprint(counts)

