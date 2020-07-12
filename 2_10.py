# Exercicio 2.10
#
# Pedro Paulo Herzog Junior		10284692
# Samuel Libardi Godoy			9805891
# Vinicius Molina Garcia		8929296

# Este script utiliza pandas + plotly express para plotar os resultados da simulação fdtd realizada
# a partir de uma fonte que gera um pulso gaussiano
# de forma a obter os resultados da fig 2.6 do Taflove

import math
import pandas as pd
import plotly.express as px
from fdtd import fdtd_gen

CONST_c = 299792458

# PARAMETROS DA SIMULAÇÃO
dt = 1e-8

dx = CONST_c * dt / 1.0005

def fonte(t): return 1 * math.exp(-((t - .4e-6) ** 2)/(.15e-6**2))

# GERADORES PARA OS DIFERENTES S
gen = fdtd_gen(fonte, dt, [(250, 1.0005)])

for n in range(180):
	U1 = next(gen)

for n in range(10):
	U2 = next(gen)

for n in range(10):
	U3 = next(gen)

# ler os resultados e fazer um grafico
data = (
	[{'x': i * dx, 'u': U1[i], 'n':180} for i in range(len(U1))]
	+ [{'x': i * dx, 'u': U2[i], 'n':190} for i in range(len(U2))]
	+ [{'x': i * dx, 'u': U3[i], 'n':200} for i in range(len(U3))]
)
fig = px.line(pd.DataFrame(data=data), x='x', y='u', color='n')
fig.show()
