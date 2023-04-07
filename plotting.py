import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")
plt.subplot(2,2,1)
x=np.arange(-5,5,0.01)
y=x**2
plt.plot(x,y,color="blue")
plt.title("$y=x^2$")

plt.subplot(2,2,2)
x=np.arange(-5,5,0.1)
y=x**3
plt.plot(x,y,color="red")
plt.title("$y=x^3$")

plt.subplot(2,2,3)
x=np.arange(-5,5,0.1)
y=np.sin(x)
plt.plot(x,y,color="black")
plt.title("$y=sin(x)$")

plt.subplot(2,2,4)
x=np.arange(-5,5,0.1)
y=np.cos(x)
plt.plot(x,y,color="green")
plt.title("$y=cos(x)$")
plt.show()

