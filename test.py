import numpy as np
lst = [x for x in range(10)]
print(lst)
for el in lst:
 print(el)
res = map(lambda x: x**2, lst)
res = list(res)
for el in res:
  print(el)

V = np.array(res)
print(V)
