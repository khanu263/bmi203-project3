import numpy as np
import heapq
from typing import Union

class Graph:

    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """ Unlike project 2, this Graph class takes an adjacency matrix as input. `adjacency_mat` 
        can either be a 2D numpy array of floats or the path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph
        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def _add_edges(self, source: int, queue: list):
        """ 

        Store edges from the given source vertex in the given priority queue.
        Each edge is stored as a tuple (i, (j, k)) where i is the weight of
        the edge and j / k are the connected vertices.

        """

        # Check that edges exist before adding them
        for i in range(0, self.adj_mat.shape[1]):
            if self.adj_mat[source][i] != 0:
                heapq.heappush(queue, (self.adj_mat[source][i], (source, i)))

    def construct_mst(self):
        """ 
        
        Given `self.adj_mat`, the adjacency matrix of a connected undirected graph, implement Prim's 
        algorithm to construct an adjacency matrix encoding the minimum spanning tree of `self.adj_mat`. 
            
        `self.adj_mat` is a 2D numpy array of floats. 

        Note that because we assume our input graph is undirected, `self.adj_mat` is symmetric. 
        Row i and column j represents the edge weight between vertex i and vertex j. An edge 
        weight of zero indicates that no edge exists. 

        """

        # Initialize structures
        dim = self.adj_mat.shape[0]
        self.mst = np.zeros((dim, dim))
        all_vertices = set(range(dim))
        visited_vertices = {0}

        # Initialize priority queue
        # (as per the docs, no need to heapify an empty list)
        queue = []
        self._add_edges(0, queue)

        # Keep going until are vertices are visited
        while visited_vertices != all_vertices:

            # Pop the lowest-weight edge
            weight, v = heapq.heappop(queue)

            # If destination vertex has not been visited:
            #  - add edge to MST
            #  - add destination vertex to visited_vertices
            #  - add new outgoing edges to priority queue
            if v[1] not in visited_vertices:
                self.mst[v[0]][v[1]] = weight
                self.mst[v[1]][v[0]] = weight
                visited_vertices.add(v[1])
                self._add_edges(v[1], queue)
