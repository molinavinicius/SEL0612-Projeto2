# Exercicio 2.7
#
# Pedro Paulo Herzog Junior		10284692
# Samuel Libardi Godoy			9805891
# Vinicius Molina Garcia		8929296

# Este script utiliza pandas + plotly express para plotar os resultados da simulação fdtd realizada
# a partir de uma fonte que gera um pulso quadrado
# de forma a obter os resultados da fig 2.3 do Taflove

import math
import pandas as pd
import plotly.express as px
from fdtd import fdtd_gen

# velocidade da luz no vaco
CONST_c = 299792458

# PARAMETROS DA SIMULAÇÃO
dt = 1e-8

dx1 = CONST_c * dt / 1
dx09 = CONST_c * dt / 0.99
dx05 = CONST_c * dt / 0.5

# FUNÇÃO DA FONTE (PULSO QUADRADO)
def fonte(t): return 1 if t < 0.3e-6 else 0

# GERADORES PARA OS DIFERENTES S
gen1 = fdtd_gen(fonte, dt, [(math.ceil(500/dx1), 1)])
gen09 = fdtd_gen(fonte, dt, [(math.ceil(500/dx09), 0.99)])
gen05 = fdtd_gen(fonte, dt, [(math.ceil(500/dx05), 0.5)])

# Simular 120 iterações
U = U09 = U05 = []
for n in range(120):
    U = next(gen1)
    U09 = next(gen09)
    U05 = next(gen05)

# ler os resultados da ultima iteração e fazer um grafico
data = (
    [{'x': i * dx1, 'u': U[i], 'S':1} for i in range(len(U))]
    + [{'x': i * dx09, 'u': U09[i], 'S':0.99} for i in range(len(U09))]
    + [{'x': i * dx05, 'u': U05[i], 'S':0.5} for i in range(len(U05))]
)
fig = px.line(pd.DataFrame(data=data), x='x', y='u', color='S')
fig.show()
