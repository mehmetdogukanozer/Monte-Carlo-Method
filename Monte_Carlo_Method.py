
import matplotlib.pyplot as plt
import math
import numpy as np
import random



alan=0
kare=0
nokta_sayisi=10000

x=np.linspace(0,2,10000)

nokta_x=[]
nokta_y=[]


for i in range(nokta_sayisi):
    nokta_x.append(random.uniform(0,2))
    nokta_y.append(random.uniform(0,4))

y=x**2
for i in range(nokta_sayisi):
    if(y[i]>nokta_y[i]):
        alan+=1
        



y_line=[[4],[4],[4]]

plt.plot((2,2),(0,4),"c--",linewidth=3)
plt.plot(y_line,"c--",linewidth=3)
plt.plot(nokta_x,nokta_y,"r.",alpha=0.2)
plt.plot(x,y,"b-",linewidth=3)
plt.grid(True)
plt.show()

print("Karenin alani = 8")
print("Toplam nokta sayimiz=10000")
print("Grafiğin altinda kalan nokta sayimiz={}".format(alan))

grafik_alani=8*(alan/nokta_sayisi)

print("Grafiğin altında kalan alan={}".format(grafik_alani))

    


