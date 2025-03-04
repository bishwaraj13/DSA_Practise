# https://www.naukri.com/code360/problems/alien-dictionary_630423
from typing import List
from collections import deque

def getAlienLanguage(dictionary: List[str], k: int) -> str:
    # create adjacency list
    adjList = [[] for _ in range(k)]

    for i in range(1, len(dictionary)):
        curr_word = dictionary[i]
        prev_word = dictionary[i-1]

        word_size = min(len(curr_word), len(prev_word))

        for j in range(word_size):
            if prev_word[j] != curr_word[j]:
                prev_char = prev_word[j]
                curr_char = curr_word[j]

                prev_int = ord(prev_char) - ord('a')
                curr_int = ord(curr_char) - ord('a')
                adjList[prev_int].append(curr_int) 
                break

    sorted_int_list = topologicalSort(adjList)
    return ''.join([chr(s + ord('a')) for s in sorted_int_list])
    

#Function to return list containing vertices in Topological order.
def topologicalSort(adj):
    V = len(adj)
    indegree = [0] * V
    answer = []
    
    # create indegree list
    for i in range(V):
        # node-th i goes to these nodes
        dest_nodes = adj[i]
        
        for node in dest_nodes:
            indegree[node] += 1
            
    queue = deque()
    
    # add nodes who has 0 indegree to queue
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        curr = queue.popleft()
        answer.append(curr)
        
        # decrement indegree for add the adjacent nodes of curr
        for node in adj[curr]:
            indegree[node] -= 1
            
            if indegree[node] == 0:
                queue.append(node)
                
    return answer