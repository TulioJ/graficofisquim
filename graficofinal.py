import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from pylab import cm


mpl.rcParams['font.family'] = 'CMU Serif, Bold Italic'
plt.rcParams['font.size'] = 18
plt.rcParams['axes.linewidth'] = 2

xa = [
0.011876415286155,
0.074496612113840,
0.141717884406487,
0.214022123057441,
0.291949761020294,
0.376107855728034,
0.467179420281882,
0.565934216841546,
0.673241265638060,
0.790083371174336,
0.917574025275803,
0.999932945693597,
]
xb = [
0.988123584713844,
0.925503387886160,
0.858282115593513,
0.785977876942559,
0.708050238979706,
0.623892144271966,
0.532820579718118,
0.434065783158454,
0.326758734361940,
0.209916628825664,
0.082425974724197,
0.000067054306403,
]

xg = [
0.026772346876488,
0.156483652895616,
0.277064184455785,
0.388970647917241,
0.492645723070029,
0.588518087343286,
0.677002454380452,
0.758499627124547,
0.833396565525552,
0.902066468948019,
0.964868873321125,
0.999972954322907,
]

xt = [
95.00,
92.00,
89.00,
86.00,
83.00,
80.00,
77.00,
74.00,
71.00,
68.00,
65.00,
63.20,
]
#for i in xa:

z = 0;

rp = 0
#pr=[]

pa = 2.3471382410
pb = 0.9893102113

#for i in xa:
#    r = (xa[z]*pa) + (xb[z]*pb) 
#    pr.append(r)
#    z = z + 1
#z = 0
#for i in xa:
#    g = ((xa[z]*pa)/((xa[z]*pa)+xb[z]*pb)) 
#    xg.append(g)
#    z = z + 1
#
#print(pr)
degree_sign = u'\N{DEGREE SIGN}'
plt.xlabel('Fração Molar Xa')
plt.ylabel('Temperatura [°C]')
plt.scatter(xa,xt)
plt.plot(xa,xt)
plt.scatter(xg,xt)
plt.plot(xg,xt)
x = [0, 0.3]
y = [82.713, 82.713]
x2 = [0.3, 0.3]
y2 = [82.713, 60]
x3 = [0.3, 0.501]
y3 = [82.713, 82.713]
x4 = [0.501, 0.501]
y4 = [82.713, 60]
plt.plot(x,y, linestyle='dashed', color ='black')
#plt.vlines(0.3, 0, 83, colors = 'black', linestyle='dashed')
plt.plot(x2, y2,linestyle='dashed', color='black')
plt.plot(x3, y3,linestyle='dashed', color='black')
plt.plot(x4, y4,linestyle='dashed', color='black')

plt.margins(0)
#plt.axhline(y=83, linestyle='dashed', color='black')



plt.show()
