#  BFS.py on artificialIntelligence Project
__author__ = " Yunindyo Prabowo "
__date__ = "Apr 14, 2017  23.45 "
def bfs_iter(graph, start, path=[]):
    """
    Iterative version of breadth first search.
    Arguments:
        graph - a dictionary of lists that is your graph and who you're connected to.
        start - the node you wish to start at
        path - a list of already visited nodes for a path
    Returns:
        path - a list of strings that equal a valid path in the graph
    """
    q=[start]
    while q:
        v = q.pop(0)
        if not v in path:
            path +=[v]
            q += graph[v]
    return path


if __name__ == '__main__':
    graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['D', 'E'], 'D': ['E'], 'E': ['A']}
    print (bfs_iter(graph, 'A'))