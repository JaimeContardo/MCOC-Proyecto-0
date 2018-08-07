#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 12:03:47 2018

@author: jaimecontardo
"""

import scipy as sp
import matplotlib.pylab as plt

x = [2.46*(10**-5), 3.73*(10**-6), 4.32*(10**-7)]
N = len(x)

#Resultados exactos de x*2
resultados_exactos = [0.00000000060516, 0.0000000000139129, 0.000000000000186624]

#Resultados para float 64
resultados_float_64 = []
for i in x:
    x_64=sp.float64(i**2)
    resultados_float_64.append(x_64)
    

#Resultados para float 32
resultados_float_32 = []
for i in x:
    x_32=sp.float32(i**2)
    resultados_float_32.append(x_32)

#Calculo de errores
error_float64 = []
error_float32 = []

i = 0
while i < N:
    error_float64.append((abs(resultados_float_64[i] - resultados_exactos[i]))/resultados_exactos[i])
    error_float32.append((abs(resultados_float_32[i] - resultados_exactos[i]))/resultados_exactos[i])
    i+=1


#Resultados por consola

print "\n"
print "Valores exactos: ", resultados_exactos, "\n"
print "Valores float 64: \n", resultados_float_64, "\n"
print "Errores float 64: \n",error_float64, "\n"
print "Valores float 32: \n", resultados_float_32, "\n"
print "Errores float 32: \n",error_float32, "\n"


#Ploteo errores
plt.figure(1)
plt.plot(x,error_float64, label="Error float 64" )
plt.plot(x,error_float32, label="Error float 32" )

plt.xlabel("x")
plt.ylabel("Error relativo f(x) = x^2")
plt.grid(True)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=1.)

plt.savefig("loss-of-significance.png")

plt.show()