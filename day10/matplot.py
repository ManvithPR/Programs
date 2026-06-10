'''import matplotlib.pyplot as plt
x1=[1,2,3]
y1=[10,20,30]
x2=[1,2,3]
y2=[30,20,10]
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()
print("Graph  created")'''

'''import matplotlib.pyplot as plt
x1=[1,2,3]
y1=[10,20,30]
plt.scatter(x1,y1,s=500)
plt.show()
print("Graph  created")'''

'''import numpy as np
import matplotlib.pyplot as plt
x1=np.linspace(0.0,5.0)
x2=np.linspace(0.0,2.0)
y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x1)
fig,(ax1,ax2)=plt.subplots(2,1)
ax1.plot(x1,y1,'o-')
ax2.plot(x2)
ax1.set_ylabel('First plot')
ax2.set_xlabel('Second plot')
ax2.set_ylabel('Y')
plt.title("Info")
plt.show()
print("Graph done")'''

'''import numpy as np
import matplotlib.pyplot as plt
np.random.seed(12123456)
z=np.random.rand(6,10)
x=np.arange(4,5,11,1)
fix,ax=plt.subplots()
ax.pcolormesh(x,y,z)
plt.title("color mesh")
plt.show()
print("graph")'''

'''import numpy as np
import matplotlib.pyplot as plt
import matplotlib
mu=100
sigma=15
fig,ax=plt.subplots()
n,bins,patches=ax.hist(mu+sigma*np.random.randn(500),50,density=True)
ax.plot(bins,((1//(np.sqrt(2*np.pi)*sigma))*np.exp(-0.5*(1/sigma*(bins-mu))**2)),'--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability Density')
fig.tight_layout()
plt.show()'''


import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,6))
ax= fig.add_subplot(111,projection='3d')
X,Y= np.meshgrid(np.arange(-4,4,0.25), np.arange(-4,4,0.25))
Z=np.sin(np.sqrt(X**2+Y**2))

ax.plot_surface(X,Y,Z,cmap='hot')
ax.contourf(X,Y,Z,zdir='z',offset=2,cmap='hot')
ax.set_zlim(-2,2)
plt.show()