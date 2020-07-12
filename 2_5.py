# Exercicio 2.5
#
# Pedro Paulo Herzog Junior		10284692
# Samuel Libardi Godoy			9805891
# Vinicius Molina Garcia		8929296

# Este script utiliza o sympy para calcular e plotar a expressão
# que define o erro relativo da velocidade de fase em relação à velocidade da luz no vácuo
# baseado nas equações 2.29, 2.30 , 2.31, 2.32 do Taflove

from math import pi
from sympy import symbols, cos, acos, sqrt, ln
from sympy.plotting import plot, PlotGrid
import sympy.plotting
from sympy.physics.units import speed_of_light as c

S = 0.5  # Numero de Courant definido para o problema

N = symbols('N')  # Variavel livre do plot (resolução de amostragem do grid)
Csi = 1 + ((1 / S) ** 2) * (cos(2 * pi * S / N) - 1)  # Eq 2.29b

trans = 2*pi*S/acos(1-2*S**2)  # Eq 2.30

# Calculo + plot da velocidade de fase normalizada
p1 = plot(
    # eq 2.32 modificada para calcular o erro percentual em relação a c
    (100*abs(2*pi / N / acos(Csi) - 1) / 1, (N, trans, 80)),
    yscale='log',
    ylim=(1e-2, 1e2),
    ylabel='erro na velocidade de fase (%)',
)
