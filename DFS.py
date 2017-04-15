#  DFS.py on  artificialIntelligence Project
__author__ = " Yunindyo Prabowo "
__date__ = "Apr 14, 2017  23.41 "

def dfs_iter(graph, start, path=[]):
    """
    Iterative version of depth first search.
    Arguments:
        graph - a dictionary of lists that is your graph and who you're connected to.
        start - the node you wish to start at
        path - a list of already visited nodes for a path
    Returns:
        path - a list of strings that equal a valid path in the graph
    """
    q=[start]
    while q:
        v = q.pop()
        if v not in path:
            path += [v]
            q += graph[v]
    return path


if __name__ == '__main__':
    graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['D', 'E'], 'D': ['E'], 'E': ['A']}
    print (dfs_iter(graph, 'A'))

