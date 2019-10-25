#analyse rolls
from collections import Counter

class Auswertung:
    def __init__(self, list):
        self.list = list
        self.dict = {}
        for i in self.list:
            self.dict[i] = self.dict.get(i, 0) + 1

    def figures(self, key):
        self.key = int(key)
        if self.key in self.dict.keys():
            total = self.dict[self.key] * self.key
            return total
        else:
            return 0

    def max(self):
        total = sum(self.list)
        return(total)

    def min(self):
        total = sum(self.list)
        return(total)

    def kenter(self):
        if len(self.dict.keys()) == 5:
            return 35
        else:
            return 0

    def full(self):
        most = Counter(self.list)
        most = most.most_common(1)[0][0]
        if len(self.dict.keys()) == 2:
            if 4 not in self.dict.values():
                return 40 + 3 * most
            else:
                return 0
        elif 5 in self.dict.values():
            return 40 + 3 * most
        else:
            return 0

    def poker(self):
        most = Counter(self.list)
        most = most.most_common(1)[0][0]
        if len(self.dict.keys()) == 2:
            if 4 in self.dict.values():
                return 50 + 4 * most
            else:
                return 0
        else:
            return 0

    def sixty(self):
        if len(self.dict) == 1:
            return 60 + sum(self.list)
        else:
            return 0

# list = [2,3,3,4,6]
# d = Auswertung(list)
# d1 = d.figures(2)
# print(d1)
