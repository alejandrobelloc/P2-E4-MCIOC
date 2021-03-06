# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:53:53 2020

@author: vjguzman
"""

from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from math import *

# Unidades base
m = 1.
kg = 1.
s = 1. 

#Unidades derivadas
N = kg*m/s**2
cm = 0.01*m
mm = 0.001*m
KN = 1000*N

Pa = N / m**2
KPa = 1000*Pa
MPa = 1000*KPa
GPa = 1000*MPa

#Parametros
L = 15.0  *m
F = 100*KN
qL = ((400*kg)/(m**2))
B = 2.0 *m
h = 3.5*m

#Inicializar modelo
ret = Reticulado()

#Nodos
ret.agregar_nodo(0     , 0   ,  0         ) #0
ret.agregar_nodo(L     , 0   ,  0         ) #1
ret.agregar_nodo(2*L   , 0   ,  0         ) #2
ret.agregar_nodo(3*L   , 0   ,  0         ) #3
ret.agregar_nodo(L/2   , B/2 , h          ) #4
ret.agregar_nodo(3*L/2 , B/2 , h          ) #5
ret.agregar_nodo(5*L/2 , B/2 , h          ) #6
ret.agregar_nodo(0     , B   , 0          ) #7
ret.agregar_nodo(L     , B   , 0          ) #8
ret.agregar_nodo(2*L   , B   , 0          ) #9
ret.agregar_nodo(3*L   , B   , 0          ) #10



#Barras
R = 8*cm
t = 5*mm

#, R, t, E, ρ, σy
props = [R, t, 200*GPa, 7850*kg/m**3, 360*MPa]


ret.agregar_barra(Barra(0, 1, *props))   # 0
ret.agregar_barra(Barra(1, 2, *props))   # 1
ret.agregar_barra(Barra(2, 3, *props))   # 2
ret.agregar_barra(Barra(3, 10, *props))  # 3
ret.agregar_barra(Barra(9, 10, *props))  # 4
ret.agregar_barra(Barra(8, 9, *props))   # 5
ret.agregar_barra(Barra(7, 8, *props))   # 6
ret.agregar_barra(Barra(0, 7, *props))   # 7
ret.agregar_barra(Barra(1, 7, *props))   # 8
ret.agregar_barra(Barra(0, 8, *props))   # 9
ret.agregar_barra(Barra(1, 8, *props))   # 10
ret.agregar_barra(Barra(2, 8, *props))   # 11
ret.agregar_barra(Barra(1, 9, *props))   # 12
ret.agregar_barra(Barra(2, 9, *props))   # 13
ret.agregar_barra(Barra(3, 9, *props))   # 14
ret.agregar_barra(Barra(2, 10, *props))  # 15
ret.agregar_barra(Barra(4, 7, *props))   # 16
ret.agregar_barra(Barra(0, 4, *props))   # 17
ret.agregar_barra(Barra(4, 8, *props))   # 18
ret.agregar_barra(Barra(1, 4, *props))   # 19
ret.agregar_barra(Barra(5, 8, *props))   # 20
ret.agregar_barra(Barra(1, 5, *props))   # 21
ret.agregar_barra(Barra(5, 9, *props))   # 22
ret.agregar_barra(Barra(2, 5, *props))   # 23
ret.agregar_barra(Barra(6, 9, *props))   # 24
ret.agregar_barra(Barra(2, 6, *props))   # 25
ret.agregar_barra(Barra(6, 10, *props))  # 26
ret.agregar_barra(Barra(3, 6, *props))   # 27
ret.agregar_barra(Barra(4, 5, *props))   # 28
ret.agregar_barra(Barra(5, 6, *props))   # 29

#ver_reticulado_3d(ret)

ret.agregar_restriccion(0, 0, 0)
ret.agregar_restriccion(0, 1, 0)
ret.agregar_restriccion(0, 2, 0)

ret.agregar_restriccion(7, 0, 0)
ret.agregar_restriccion(7, 1, 0)
ret.agregar_restriccion(7, 2, 0)

ret.agregar_restriccion(3, 1, 0)
ret.agregar_restriccion(3, 2, 0)

ret.agregar_restriccion(10, 1, 0)
ret.agregar_restriccion(10, 2, 0)


# Carga viva
qL_A1 = -qL*(7.5*m**2)
qL_A2 =  -qL*(15*m**2)

ret.agregar_fuerza(0, 2, qL_A1)
ret.agregar_fuerza(3, 2, qL_A1)
ret.agregar_fuerza(7, 2, qL_A1)
ret.agregar_fuerza(10, 2, qL_A1)

ret.agregar_fuerza(1, 2, qL_A2)
ret.agregar_fuerza(2, 2, qL_A2)
ret.agregar_fuerza(8, 2, qL_A2)
ret.agregar_fuerza(9, 2, qL_A2)


# Carga muerta
peso = ret.calcular_peso_total()
qD = ((peso)/(90*m**2))
qD_A1 = -qD*(7.5*m**2)
qD_A2 =  -qD*(15*m**2)

ret.agregar_fuerza(0, 2, qD_A1)
ret.agregar_fuerza(3, 2, qD_A1)
ret.agregar_fuerza(7, 2, qD_A1)
ret.agregar_fuerza(10, 2, qD_A1)

ret.agregar_fuerza(1, 2, qD_A2)
ret.agregar_fuerza(2, 2, qD_A2)
ret.agregar_fuerza(8, 2, qD_A2)
ret.agregar_fuerza(9, 2, qD_A2)


#ver_reticulado_3d(ret, axis_Equal=False)


ret.ensamblar_sistema()
ret.resolver_sistema()
f = ret.recuperar_fuerzas()

print(ret)

ver_reticulado_3d(ret, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 30.,
        "ver_factor_utilizacion": True
    },
    opciones_barras = {
        "color_barras_por_fu": True,
        "ver_numeros_de_barras": True,
        "ver_fuerza_en_barras": True
    }, axis_Equal=False)


'''
barras_a_rediseñar = [3,4,5, 9, 10, 11]
barras = ret.obtener_barras()
for i in barras_a_rediseñar:
	barras[i].rediseñar(f[i])
'''


'''
ret.ensamblar_sistema()
ret.resolver_sistema()
f1 = ret.recuperar_fuerzas()

peso = ret.calcular_peso_total()

print(f"peso = {peso}")

ver_reticulado_3d(ret, 
    opciones_nodos = {
        "usar_posicion_deformada": True,
        "factor_amplificacion_deformada": 30.,
    },
    opciones_barras = {
        "color_barras_por_fu": True,
        "ver_numeros_de_barras": True,
        "ver_fuerza_en_barras": True
    })
'''