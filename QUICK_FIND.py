
class QuickFind:
    def __init__(self, size):
        self.size = size
        self.id_ary = [i for i in range(self.size)]

    def find(self, p, q):
        return self.id_ary[p] == self.id_ary[q]

    def union(self, p, q):
        for obj_idx, obj_id in enumerate(self.id_ary):
            if obj_id == self.id_ary[p]:
                self.id_ary[obj_idx] = self.id_ary[q]
            else:
                pass
        

test_ary = QuickFind(size = 5)
print("Sample Array: ", test_ary.id_ary)
print("Check Connection: ", test_ary.find(0,1))
test_ary.union(0,4)
print("Check Array: ", test_ary.id_ary)
print("Check Connection: ", test_ary.find(0,4))

