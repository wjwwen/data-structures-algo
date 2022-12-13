s=set()

t={1,3}
s.add(2)
t.add(2)
print(s,t)

s.add(5)
t.add(5)
print(s,t)

s.add(2)
t.add(2)
print(s,t)

import random
z = {x for x in range(100)}
while len(z) > 1:
    p = random.randint(0, 99)
    try:
        z.remove(p)
    except:
        pass
print(z)

