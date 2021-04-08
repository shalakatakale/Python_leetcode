bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

b = set(bank)
print(b)


start = "AAAAACCC"
s = {start}
print(s)

q = [(start, 0)]
print(q)
top, d = q.pop(0)
print(top, d)
visited = set()
visited.add(top)
print(visited)


from collections import defaultdict
graph = defaultdict(lambda:set())
print(graph)

graph1 = defaultdict(lambda:0)
print('graph1', graph1)

graph2 = defaultdict()
print('graph2', graph2)

x = defaultdict(int)
print('x', x)

from collections import OrderedDict
c = OrderedDict(5)
print(c)
