# https://leetcode.com/problems/accounts-merge/
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * (n)
        self.size = [1] * (n)
    
    def findUltimateParent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.findUltimateParent(self.parent[x])
        return self.parent[x]
    
    def unionByRank(self, x, z):
        x_root = self.findUltimateParent(x)
        z_root = self.findUltimateParent(z)
        
        if x_root == z_root:
            return
        
        if self.rank[x_root] < self.rank[z_root]:
            self.parent[x_root] = z_root
        elif self.rank[x_root] > self.rank[z_root]:
            self.parent[z_root] = x_root
        else:
            self.parent[x_root] = z_root
            self.rank[z_root] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        mapMailNode = {}
        ds = DisjointSet(n)

        for i in range(n):
            account = accounts[i]
            # iterate over all the emails
            for j in range(1, len(account)):
                email = account[j]

                if email not in mapMailNode:
                    mapMailNode[email] = i
                else:
                    ds.unionByRank(i, mapMailNode[email])

        # Create merged accounts
        mergedAccounts = [[] for _ in range(n)]

        # Group emails by ultimate parent
        for email, node in mapMailNode.items():
            ultimateParent = ds.findUltimateParent(node)
            mergedAccounts[ultimateParent].append(email)

        # Format the final result
        result = []
        for i in range(n):
            if mergedAccounts[i]:
                # Sort the emails as required
                mergedAccounts[i].sort()
                # Add the name at the beginning
                account = [accounts[i][0]] + mergedAccounts[i]
                result.append(account)
        
        return result
