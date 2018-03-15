import math
import helpers
import heapq

def shortest_path(M,start,goal):
    ## initialize
    frontier = set()
    priority_queue = []
    explored = set()
    path = []

    ## calculate Distance between two nodes
    def heuristic(a,b):
        '''the heuristic function return the heuristic from goal to
        all nodes. i use the Euclidian Distance in the case'''
        h = math.sqrt ((M.intersections[a][0] - M.intersections[b][0])**2 + (M.intersections[a][1] - M.intersections[b][1])**2)
        return h

    ## initialize start node
    node = {}
    node[start] = {'g': 0,
                    'h': heuristic(start, goal),
                    'f': 0 + heuristic(start, goal),
                    'parent': None }

    ## add start to frontier
    frontier.add(start)

    ## add start to Priority Queue
    heapq.heappush(priority_queue, (node[start]['f'], start))

    ## search for the shortest_path
    while frontier:
        # choose the node current_node which has the min(f) as the searching node
        current_node = heapq.heappop(priority_queue)[1]

        # then search the neighbors of node current_node , update
        for neighbor in M.roads[current_node]:
            # choose neighbors that is not in explored
            if neighbor not in explored:
                # update neighbors
                if (neighbor not in frontier) or ((node[current_node]['g'] + \
                heuristic(current_node, neighbor) + heuristic(neighbor, goal)) < \
                node[neighbor]['f']):
                    node[neighbor] = {'g': node[current_node]['g'] + heuristic(current_node, neighbor),
                                       'h': heuristic(neighbor, goal),
                                       'f': node[current_node]['g'] + heuristic(current_node, neighbor)+heuristic(neighbor, goal),
                                       'parent': current_node }
                    # add neighbor to frontier
                    frontier.add(neighbor)
                    # add neighbor to priority_queue
                    heapq.heappush(priority_queue, (node[neighbor]['f'], neighbor))

        ## move current_node from frontier to explored
        if current_node in frontier:
            frontier.remove(current_node)
            explored.add(current_node)
            
        

        ## if goal has been in explored, the search is done, contruct the path and break
        if  goal in explored:
            i = goal
            while i:
                path.append(i)
                i = node[i]['parent']
            path.reverse()
            break
    return path 

