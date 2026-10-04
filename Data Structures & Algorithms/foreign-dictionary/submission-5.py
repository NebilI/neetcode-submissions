
from collections import deque
from typing import List


class Solution:
    def compare_words(self, w1, w2):
        i = 0

        while i < min(len(w1), len(w2)):
            if w1[i] != w2[i]:
                return (w1[i], w2[i])
            i += 1

        # Invalid ordering: a longer word comes before its prefix.
        if len(w1) > len(w2):
            return False

        # No ordering constraint.
        return None

    def compose_graph(self, words):
        # Include every unique character, even isolated characters.
        graph = {letter: [] for word in words for letter in word}

        for i in range(len(words) - 1):
            order = self.compare_words(words[i], words[i + 1])

            if order is False:
                return None

            if order is not None:
                first, second = order

                # Avoid duplicate edges.
                if second not in graph[first]:
                    graph[first].append(second)

        return graph

    def topological_sort(self, graph):
        # Initialize indegrees for every character.
        indegree = {node: 0 for node in graph}

        for neighbors in graph.values():
            for neighbor in neighbors:
                indegree[neighbor] += 1

        # Start with every character that has no prerequisites.
        queue = deque(
            node for node in indegree
            if indegree[node] == 0
        )

        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If some characters remain, the graph contains a cycle.
        if len(order) != len(graph):
            return None

        return order

    def foreignDictionary(self, words: List[str]) -> str:
        graph = self.compose_graph(words)

        if graph is None:
            return ""

        letters = self.topological_sort(graph)

        if letters is None:
            return ""

        return "".join(letters)
