import pytest
from pygraph.pygraph import create_graph  # 修改导入路径


@pytest.fixture
def sample_graph():
    g = create_graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "A", 5)
    return g


def test_add_vertex(sample_graph):
    assert "D" not in sample_graph.get_vertices()
    sample_graph.add_vertex("D")
    assert "D" in sample_graph.get_vertices()


def test_add_edge(sample_graph):
    edges = sample_graph.get_edges()
    assert ("A", "B", 1) in edges
    assert ("C", "A", 5) in edges


def test_dfs(sample_graph):
    # DFS 结果可能有多种有效顺序
    dfs_result = sample_graph.depth_first_search("A")
    assert set(dfs_result) == {"A", "B", "C"}
    assert dfs_result[0] == "A"
    assert len(dfs_result) == 3


def test_bfs(sample_graph):
    # BFS 应该有确定顺序
    assert sample_graph.breadth_first_search("A") == ["A", "B", "C"]


def test_neighbors(sample_graph):
    assert sample_graph.get_neighbors("A") == [("B", 1)]
    assert sample_graph.get_neighbors("B") == [("C", 1)]
    assert sample_graph.get_neighbors("C") == [("A", 5)]
