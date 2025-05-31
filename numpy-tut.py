import numpy as np
a = np.arange(25).reshape(5,5)

# b = a[:,1::2]
# print(b)

# c = a[-1]
# print(c)
a.__setitem__(0,[100.101,102,103,104,105])
print(a.__getitem__(0))
# d = a[1::2, :3:2 ]
# print(d)

