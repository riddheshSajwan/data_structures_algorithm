import heapq

h = [11,2,33,4,12]
heapq.heapify(h)
print(h)
heapq.heappush(h,1)
print(h)
heapq.heappop(h)
print(h)
heapq.heapreplace(h,67)
print(h)
print(heapq.heappushpop(h,29))
print(h)