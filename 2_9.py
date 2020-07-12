# Exercicio 2.9
#
# Pedro Paulo Herzog Junior		10284692
# Samuel Libardi Godoy			9805891
# Vinicius Molina Garcia		8929296

# Este script utiliza pandas + plotly express para plotar os resultados da simulação fdtd realizada
# de forma a obter os resultados da fig 2.5 do Taflove

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
gen = fdtd_gen(fonte, dt, [(180, 1), (40, 0.25)])

for n in range(270):
	U1 = next(gen)

# ler os resultados e fazer um grafico
data = (
	[{'x': i * dx, 'u': U1[i], 'n':270} for i in range(len(U1))]
)
fig = px.line(pd.DataFrame(data=data), x='x', y='u', color='n')
fig.show()
