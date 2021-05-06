
class QuickUnion:
    def __init__(self, size):
        self.size = size
        self.id_ary = [i for i in range(self.size)]

    def root(self, obj_idx):
        while self.id_ary[obj_idx] != obj_idx:
            obj_idx = self.id_ary[obj_idx]
        return obj_idx

    def find(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        self.id_ary[self.root(p)] = self.id_ary[self.root(q)]
        


size = 8
test_ary = QuickUnion(size = size)

print("Check Array:")
print([i for i in range(size)])
print(test_ary.id_ary)
print("Check Connection: ", test_ary.find(0,1))

test_ary.union(0,4)
test_ary.union(4,5)
test_ary.union(1,5)
test_ary.union(6,7)

print("\nCheck Array:")
print([i for i in range(size)])
print(test_ary.id_ary)
print("Check Connection: ", test_ary.find(4,6))

test_ary.union(2,6)
test_ary.union(2,4)

print("\nCheck Array:")
print([i for i in range(size)])
print(test_ary.id_ary)
print("Check Connection: ", test_ary.find(4,6))