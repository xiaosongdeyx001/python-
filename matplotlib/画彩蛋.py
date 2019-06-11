import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
import numpy as np
fig=plt.figure()
#projection='3d'的意思是绘制三维图形，否则绘制的就是平面图形，彩蛋就不会那么立体了
ax=fig.gca(projection='3d')
u = np.linspace(0,2*np.pi,1000)
v = np.linspace(0,2*np.pi,1000)

x=10*np.outer(np.cos(u),np.sin(v))
y=10*np.outer(np.sin(u),np.sin(v))
z=6*np.outer(np.ones(np.size(u)),np.cos(v))
ax.plot_surface(x,y,z,cmap='rainbow')
#plt.cm.get_cmap(value))

plt.plot([-15,0,10],[0,0,0],[0,0,0],color='indigo',linestyle='--')
plt.plot([0,0,0],[-15,0,10],[0,0,0],color='indigo',linestyle='--')
plt.plot([0,0,0],[0,0,0],[-10,0,6],color='indigo',linestyle='--')
ax.quiver(0, 0, 6, 0, 0, 5, length=1, color='indigo',linestyle='--')
ax.quiver(0, 10, 0, 0, 5, 0, length=1, color='indigo',linestyle='--')
ax.quiver(10, 0, 0, 5, 0, 0, length=1, color='indigo',linestyle='--')
print(plt.cm.cmap_d.keys())
plt.show()

ims=[Image.open(filepath+"\\"+fn) for fn in listdir(filepath) if fn.endswith('.png')]
#columns的意思是一行包括几个彩蛋，如果等于5，每行就是五个彩蛋，第六个彩蛋就会出现在下一行
result=Image.new(ims[0].mode,(width*rows,math.ceil(height*len(ims)/rows)))

for i,im in enumerate(ims):
    row=math.floor(i/rows)
    column=i%rows
    result.paste(im,box=(column*width,row*height))

