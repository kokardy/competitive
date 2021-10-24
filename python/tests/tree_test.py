from competitive.tree import Tree


def test_tree():
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

    print(
        """
    0---1---6---8
        |   |---7
        |
        |---2---3
            |---9
            |---4---5
            """
    )
    tree.add_edges(edges)
    expected = (4, 5)
    start = 0
    max_depth = 0
    max_depth_node = start

    print("-----bfs-----")
    for depth, node in tree.bfs(0):
        print(f"depth: {depth} node: {node}")
        if depth > max_depth:
            max_depth = depth
            max_depth_node = node

    assert (max_depth, max_depth_node) == expected

    print("-----dfs-----")
    for depth, node in tree.dfs(0):
        print(f"depth: {depth} node: {node}")
        if depth > max_depth:
            max_depth = depth
            max_depth_node = node

    assert (max_depth, max_depth_node) == expected
