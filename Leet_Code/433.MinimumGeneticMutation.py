# Twitter 433. Minimum Genetic Mutation
class Solution:
    def minMutation(self, start, end, bank):
        self.graph = defaultdict(lambda: set())

        def build_graph(node):
            choices = ['A', 'C', 'G', 'T']
            for i in range(len(node)):
                for c in choices:
                    test = list(node)
                    test[i] = c
                    test = ''.join(test)
                    if test in bank and node != test:
                        self.graph[node].add(test)
                        self.graph[test].add(node)

        build_graph(start)
        for word in bank:
            build_graph(word)

        q = [(start, 0)]
        visited = set()
        #while q:
            #top, d = q.pop(0)  # d gives number of mutations done
            # use above 2 lines or below for line
        for top, d in q:
            if top == end:
                return d
            for nxt in self.graph[top]:
                if nxt not in visited:
                    q.append((nxt, d + 1))
                    visited.add(nxt)
            print(q)
        return -1
# Amazing
class Solution(object):
     def minMutation(self, start, end, bank):
        bank, visited, q = set(bank), {start}, [(start, 0)]
        for g,k in q:
            for s in (g[:i] + cc + g[i+1:] for i,c in enumerate(g) for cc in 'ACGT'):
                if s in bank and s not in visited:
                    q.append((s, k+1))
                    visited.add(s)
                    if s==end:
                        return k+1
            print(q)
        return -1


