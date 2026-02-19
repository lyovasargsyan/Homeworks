# 1․ Գրել MyList class, որը կունենա գրեթե բոլոր այն մեթոդները և ֆունկցիոնալությունը, որը ունի list class-ը առանց ժառանգելու։
#    Կլասի ներսում կարող եք պահել լիստ և օգտագործել լիստի մեթոդները։
#    Ավելացրեք մեթոդներ, որոնք կուզեիք, որ լիստերն ունենային, բայց չունեն։


class MyList:
    def __init__(self, data=None):
        if data is None:
            self.lst = []
        else:
            self.lst = list(data)

    def __repr__(self):
        return f"MyList({self.lst})"

    def len__(self):
        return len(self.lst)

    @property
    def item__(self, index):
        return self.lst[index]
    
    @item__.setter
    def item__(self, index, value):
        self.lst[index] = value

    @item__.deleter
    def item__(self, index):
        del self.lst[index]

    def append(self, item):
        self.lst.append(item)


    def insert(self, index, item):
        self.lst.insert(index, item)

    def remove(self, item):
        self.lst.remove(item)

    def pop(self, index=-1):
        return self.lst.pop(index)

    def clear(self):
        self.lst = []

    def index(self, item):
        return self.lst.index(item)

    def count(self, item):
        return self.lst.count(item)

    def reverse(self):
        return self.lst.reverse()


    def frequency(self):
        counts = {}
        for item in self.lst:
            counts[item] = counts.get(item, 0) + 1
        return counts
    
    def sum(self):
        return sum(self.lst)

    def average(self):
        return sum(self.lst) / len(self.lst) if self.lst else 0
    
    def unique(self):
        s = set()
        res = []
        for x in self.lst:
            if x not in s:
                res.append(x)
                s.add(x)
        return MyList(res)