from collections import defaultdict
from heapq import *
import time
import random
def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    pred = {}
    q, seen = [(0,f,())], set()

    for edge in edges:
        pred[edge] = None
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                node = v1
                nodes = []
                while True:
                    nodes.append(node)
                  #  print(node)
                    if node not in pred:
                        break
                    node = pred[node]
                nodes.reverse()
                return (cost, nodes)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))
                    pred[v2] = v1

    return float("inf")

if __name__ == "__main__":

    edges = []
    def create_seats(amount):
        global edges
        for i in range(amount):
            chair_distance  =  random.randint(2, 10)
            edges.append(("Stand@None", "Sit@Chair_{}".format(i), 1 + chair_distance))
            edges.append(("Stand@None&plate@hands", "Sit@Chair_{}&plate@hands".format(i), 1 + chair_distance))
            edges.append(("Stand@None&plate@hands", "Sit@Chair_{}&plate@table".format(i), 0.5 + chair_distance))
            edges.append(("Sit@Chair_{}&plate@hands".format(i), "Sit@Chair_{}&plate@table".format(i), 0.5 + chair_distance))
            edges.append(("Sit@Chair_{}&plate@table".format(i), "Stand@None".format(i), 1 + chair_distance))

    def create_kitchens(amount):
        global edges
        for i in range(amount):
            kitchen_distance = random.randint(6, 12)
            edges.append(("Stand@None", "GetFood@Fridge_{}".format(i), 1 + kitchen_distance))
            edges.append(("GetFood@Fridge_{}".format(i), "CookFood@Stove_{}".format(i), 1 + 1))
            edges.append(("CookFood@Stove_{}".format(i), "Stand@None&plate@hands", 0.5 + 0))

    def create_random_edges():
        create_kitchens(5)
        create_seats(100)


    def test_random_edges():
        destination_edge_idx = 1
        nodes_seen = []
        for edge in edges:
           if edge[destination_edge_idx] not in nodes_seen:
               nodes_seen.append(edge[destination_edge_idx])
        print("There are {} nodes".format(len(nodes_seen)))
        print("There are {} edges".format(len(edges)))
        old_time = time.time()

        for i in range(5 * 1):

            for edge in edges:
                if "plate@" in edge[destination_edge_idx]:
                    result = dijkstra(edges, "Stand@None&plate@hands", edge[destination_edge_idx])
                #print(edge[destination_edge_idx])
                    print(result)
        new_time = time.time()
        print("It took me {} ms to do this!".format((new_time - old_time) * 1000))
    print ("=== Dijkstra ===")
    print (edges)
    create_random_edges()
    test_random_edges()
