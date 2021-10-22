from main.tree import Tree


def test__tree():
    tree = Tree(10)
    edges = (
        (0, 1),
        (1, 6),
        (6, 8),
        (6, 7),
        (1, 2),
        (2, 3),
        (2, 9),
        (2, 4),
        (4, 5),
    )
    tree.add_edges(edges)
    expected = (4, 5)
    start = 0
    max_depth = 0
    max_depth_node = start

    for depth, node in tree.bfs(0):
        if depth > max_depth:
            max_depth = depth
            max_depth_node = node

    assert (max_depth, max_depth_node) == expected
