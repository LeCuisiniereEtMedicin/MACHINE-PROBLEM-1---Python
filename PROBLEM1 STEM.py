import numpy as np
import matplotlib.pyplot as plot
#Initial input of variable n
a = list(range(100))
x = np.array([()])
y = np.array([()])
for j in a:
    n = j
    while True:
        #Output of satisfactory number
        if n <= 9:
            fn = n*n - 7
            y = np.append(y,fn)
            break
        #For n >= 10
        else:
            n = n%10
            fn = n*n - 7
            y = np.append(y,fn)
            break
plot.stem(a,y)