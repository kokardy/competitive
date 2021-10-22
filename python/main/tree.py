from typing import List, Dict, Union, Set, Tuple, Generator, Iterable, Deque
from collections import defaultdict
from collections import deque


class Tree:
    def __init__(self, n: int):
        self.nodes: Union[List[Set[int]], Dict[int, Set[int]]]
        if n <= 10 ** 5:
            self.nodes = [set() for _ in range(n)]
        else:
            self.nodes = defaultdict(set)

    def add_edge(self, node_pair: Tuple[int, int]):
        n1 = node_pair[0]
        n2 = node_pair[1]
        self.nodes[n1].add(n2)
        self.nodes[n2].add(n1)

    def add_edges(self, node_pairs: Iterable[Tuple[int, int]]):
        for node_pair in node_pairs:
            self.add_edge(node_pair)

    def bfs(self, start_node: int) -> Generator[Tuple[int, int], None, None]:
        queue: Deque[Tuple[int, int]] = deque()
        queue.append((0, start_node))
        while len(queue) > 0:
            for _ in range(len(queue)):
                depth_node = queue.popleft()
                yield depth_node
                depth, node = depth_node
                queue.extend(((depth + 1, sub_nodes) for sub_nodes in self.nodes[node]))
