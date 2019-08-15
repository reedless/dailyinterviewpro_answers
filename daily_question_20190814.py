'''
Given an undirected graph, determine if a cycle exists in the graph.

Can you solve this in linear time, linear space?
'''
def find_cycle_helper(graph, reached):
    if (graph == {}):
        return False
    result = False
    for key in graph.keys():
        if (key in reached):
            return True
        else:
            reached.append(key)
            result = find_cycle_helper(graph[key], reached) or result
    return result


def find_cycle(graph):
    return find_cycle_helper(graph, [])


graph = {
    'a': {'a2':{}, 'a3':{} },
    'b': {'b2':{}},
    'c': {}
}
print (find_cycle(graph))
# False
graph['c'] = graph
print (find_cycle(graph))
# True
