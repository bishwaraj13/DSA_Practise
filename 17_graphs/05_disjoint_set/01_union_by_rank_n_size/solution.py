class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)
    
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

    def unionBySize(self, x, z):
        x_root = self.findUltimateParent(x)
        z_root = self.findUltimateParent(z)

        if x_root == z_root:
            return
        
        if self.size[x_root] < self.size[z_root]:
            self.parent[x_root] = z_root
            self.size[z_root] += self.size[x_root]
        else:
            self.parent[z_root] = x_root
            self.size[x_root] += self.size[z_root]

if __name__ == "__main__":
    ds = DisjointSet(7)
    ds.unionByRank(1, 2)
    ds.unionByRank(2, 3)
    ds.unionByRank(4, 5)
    ds.unionByRank(6, 7)
    ds.unionByRank(5, 6)

    # check if 3 and 7 are same
    if ds.findUltimateParent(3) == ds.findUltimateParent(7):
        print(f"{3} and {7} have same ultimate parent")
    else:
        print(f"{3} and {7} dont have same ultimate parent")

    ds.unionByRank(3, 7)

    # check if 3 and 7 are same
    if ds.findUltimateParent(3) == ds.findUltimateParent(7):
        print(f"{3} and {7} have same ultimate parent")
    else:
        print(f"{3} and {7} dont have same ultimate parent")
