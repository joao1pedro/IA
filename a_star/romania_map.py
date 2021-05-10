from create_graph import create_graph
from vertex import *
from graph import *
import queue
import os
import sys 



def a_star(graph, start, end):
    cost = 0

    #borda
    edge = queue.PriorityQueue()
    edge.put((0, 0, [start]))
    exploited = []

    while not edge.empty():
        u = edge.get()
        
        if end in u[2]:
            return ' -> '.join(u[2]) + '\ncost: ' + str(u[1])

        cost = u[1]
        exploited.append(u[2][-1])
        for neighbor in graph.getEdges(u[2][-1]):
            if neighbor[0] not in exploited:
                path = u[2][:]
                path.append(neighbor[0])
                edge.put((graph.getCost(neighbor[0]) + neighbor[1], cost + neighbor[1], path))


graph = create_graph()
print(a_star(graph, sys.argv[1], sys.argv[2]))
