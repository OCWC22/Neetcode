import collections

d = collections.deque([1,2,3,4,5])
print(d)

d.append(100)
print(d)

d.appendleft(400)
print(d)

d.popleft()
print(d)

d.insert(1,5959)
print(d) 