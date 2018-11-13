from random import randint
class SortUp:
    def __init__(self, posl):
        self.posl = posl; self.counter = 0; self.res = []
        for i in range(len(self.posl)):
          for j in range(i,len(self.posl)):
            if self.posl[i] > self.posl[j]:
              self.posl[i],self.posl[j] = self.posl[j],self.posl[i]
          self.res.append(self.posl[i])
    def __iter__(self):
        return self
    def __next__(self):
      if self.counter < len(self.posl):
        self.counter += 1
        return self.res[self.counter-1]
      else:
        raise StopIteration
s = [1,3,-1,0,5,6,7,-2,2,7]
res = [x for x in SortUp(s.copy())]
print (res, s) 