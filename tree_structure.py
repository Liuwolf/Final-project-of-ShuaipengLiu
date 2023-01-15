import os
from priority_queue import MiniumPriorityQueue
from graphviz import Digraph

os.environ['PATH'] = os.pathsep + r'D:\soft\Graphviz\bin'
queue = MiniumPriorityQueue()
data = [4, 5, 9, 12, 2, 8, 7]
for k in data:
    queue.insert(k)
tree = queue.bt
dot_data = Digraph(comment="Queue's Tree Structure")
edges = []
for i in range(tree.s):
    dot_data.node(str(i), str(tree.get(i)))
    lp = 2 * i + 1
    rp = 2 * i + 2
    if lp < tree.s:
        dot_data.node(str(lp), str(tree.get(lp)))
        edges.append(str(i) + str(lp))
    if rp < tree.s:
        dot_data.node(str(rp), str(tree.get(rp)))
        edges.append(str(i) + str(rp))
dot_data.edges(edges)
dot_data.render('./Tree-Structure.gv', view=True)



