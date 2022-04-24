'''
self.ids is dictionary, where for each person(id) we will keep pair (station, time) if the last action this person did is check In and empty if it was check OUt
self.pairs is counter, where for each pair of stations we keep total time spend between two stations.
self.freqs is counter, where for each pair of stations we keep how many trips we have between these two stations.
Now, let us discuss, what our functions will do:

checkIn(self, id, stationName, t): we just put pair (stationName, t) into self.ids[id].
checkOut(self, id, stationName, t). Here we look at person id, extract information about his last station visited (pop it from self.ids[id] and update self.pairs, self.freqs for these pairs of stations.
getAverageTime(self, startStation, endStation): here we just look at dictionaries self.pairs and self.freqs and directly return result.
Complexity: time compexlty is O(1) for all 3 operations. Space complexity potentially is O(Q), where Q is toatl number of queries.
'''
class UndergroundSystem:
    def __init__(self):
        self.ids = {}
        self.pairs = Counter()
        self.freqs = Counter()
        
    def checkIn(self, id, stationName, t):
        self.ids[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        Name2, t2 = self.ids.pop(id)
        self.pairs[(Name2, stationName)] += t-t2
        self.freqs[(Name2, stationName)] += 1
        
    def getAverageTime(self, startStation, endStation):
        return self.pairs[startStation, endStation]/self.freqs[startStation, endStation]
