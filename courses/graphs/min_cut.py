import copy
import functools
import random


def retries(n=1):
    results = []

    def inner(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            if kwargs.get("start"):
                for _ in range(n):
                    _args = copy.deepcopy(args)
                    _kwargs = copy.deepcopy(kwargs)
                    results.append(func(*_args, **_kwargs))
                return results
            else:
                return func(*args, **kwargs)

        return wrap

    return inner


def load_data(path):
    adjacency_dict = {}
    for row in open(path).readlines():
        node_id, *edges = row.strip().split("\t")
        adjacency_dict[node_id] = edges
    return adjacency_dict


@retries(15)
def min_cut(adjacency_dict: dict, start=False):
    if len(adjacency_dict) > 2:
        node1_id = random.choice(list(adjacency_dict.keys()))
        node2_id = random.choice(adjacency_dict[node1_id])
        node1_edges: list = adjacency_dict[node1_id]
        node2_edges: list = adjacency_dict.pop(node2_id)
        node1_edges = node1_edges + node2_edges
        for node in node1_edges.copy():
            if node == node1_id or node == node2_id:
                node1_edges.remove(node)
        adjacency_dict[node1_id] = node1_edges
        for node, edges in adjacency_dict.copy().items():
            if len(edges) == 0:
                adjacency_dict.pop(node)
                continue
            for edge in [edge for edge in edges if edge == node2_id]:
                adjacency_dict[node].remove(edge)
                adjacency_dict[node].append(node1_id)
        return min_cut(adjacency_dict)
    else:
        min_c = 0
        for edges in adjacency_dict.values():
            min_c += len(edges)
        return min_c / 2
