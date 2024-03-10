import os
import networkx as nx
from collections import deque
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Validation:
    def __init__(self, state_chart):
        self.state_chart_bfs = state_chart

    def graph_build(self):
        """Builds two directed graphs for validation and state removal."""
        try:
            validation_bfs = nx.DiGraph()
            reverse_graph = nx.DiGraph()
            node_lis = set()

            for state_node in self.state_chart_bfs:
                node_lis.add(state_node)
                transitions = self.state_chart_bfs[state_node].get("transitions", [])
                
                for trans in transitions:
                    target = trans.get("target")
                    if target:
                        validation_bfs.add_edge(state_node, target, label = trans.get("event"))
                        reverse_graph.add_edge(target, state_node)

            return validation_bfs, reverse_graph, node_lis
        except Exception as e:
            logger.error(f"Error in graph_build: {e}")
            raise

    def bfs(self, graph, start_node):
        """Performs BFS on the graph starting from start_node."""
        if start_node not in graph:
            logger.error(f"Start node {start_node} not found in the graph.")
            return set()

        visited = set()
        queue = deque([start_node])

        while queue:
            current_node = queue.popleft()
            if current_node not in visited:
                visited.add(current_node)
                queue.extend([n for n in graph.neighbors(current_node) if n not in visited])

        return visited

    def validation_check(self, graph_bfs, start_node, node_lis, name_new_state):
        """Checks if the graph is valid after operation."""
        try:
            if name_new_state is None or not isinstance(name_new_state, str):
                raise ValueError("Invalid new state name.")

            vis_lis = self.bfs(graph_bfs, start_node)
            node_lis.add(name_new_state)

            vis_lis = [element for element in vis_lis if element not in [None, ""]]
            node_lis = [element for element in node_lis if element not in [None, ""]]
            print("Visited nodes from the current state: ")
            print(vis_lis)
            print("Non Visited nodes from the current state: ")
            result = list(set(node_lis) - set(vis_lis))
            print(result)
            return vis_lis == node_lis
        except Exception as e:
            logger.error(f"Error in validation_check: {e}")
            return False
