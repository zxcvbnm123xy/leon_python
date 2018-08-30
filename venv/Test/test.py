import numpy as np
a=np.array([1,2,3])
print(a)

# 多于一个维度
import numpy as np
a1 = np.array([[1,  2],  [3,  4]])
print(a1)

# 最小维度
import numpy as np
a2 = np.array([1,  2,  3,4,5], ndmin =  2)
print(a2)

# dtype 参数
import numpy as np
a3 = np.array([1,  2,  3], dtype = complex)
print(a3)

import numpy as np
a4 = np.arange(0,60,5)
a4 = a4.reshape(3,4)
print ('原始数组是：')
print (a4,'\n' )
print ('修改后的数组是：' )
for x in np.nditer(a4):
    print (x,)
