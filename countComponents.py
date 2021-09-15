Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

class Solution
      def countComponents(self, n: int, edges: List[List[int]]) -> int:
          par = [i for i in range(n)]
          rank = [1] * n
        
          # Find root parent
          def find(n1):
              res = n1
          
              while res != par[res]:
                # path compression by setting parent of result equal to its grandparent
                  res = par[par[res]]
                  res = par[res]
              return res
          
          
          def union(n1, n2):
              p1, p2 = find(n1), find(n2)
          
              if p1 == p2:
                  return 0
          
              if rank[p2] > rank[p1]:
                  par[p1] = p2
                  rank[p2] += rank[p1]
              else:
                  par[p2] = p1
                  rank[p1] += rank[p2]
              return 1
            
          res = n
          for n1, n2 in edges:
              res = union(n1, n2)
          return res
