# Exercicio 2.4
#
# Pedro Paulo Herzog Junior		10284692
# Samuel Libardi Godoy			9805891
# Vinicius Molina Garcia		8929296

# Este script utiliza o sympy para calcular e plotar as expressões
# que definem a velocidade de fase normalizada e constante de atenuação por unidade do grid
# baseado nas equações 2.29, 2.30 , 2.31, 2.32, e 2.37 do Taflove
# Os plots foram feitos em figuras separadas por limitação da plataforma utilizada

from math import pi
from sympy import symbols, cos, acos, sqrt, ln
from sympy.plotting import plot, PlotGrid
import sympy.plotting
from sympy.physics.units import speed_of_light as c

S = 1/sqrt(2)  # Numero de Courant definido para o problema

N = symbols('N')  # Variavel livre do plot (resolução de amostragem do grid)
Csi = 1 + ((1 / S) ** 2) * (cos(2 * pi * S / N) - 1)  # Eq 2.29b

trans = 2*pi*S/acos(1-2*S**2)  # Eq 2.30

# Calculo + plot da velocidade de fase normalizada
p1 = plot(
    (2*pi / N / acos(Csi), (N, trans, 10)),  # eq 2.32 (normalizada)
    (2 / N, (N, 1, trans)),  # eq 2.37a (normalizada)
    ylabel='vp/c (normalizada)',
    show=False
)

# Calculo + plot da constante de atenuação
p2 = plot(
    (-ln(-Csi - sqrt(Csi ** 2 - 1)), (N, 1, trans)),
    ylim=(0, 6),
    xlim=(1, 10),
    line_color='red',
    ylabel='αΔx (Np/célula do grid)',
    show=False
)

PlotGrid(1, 2, p1, p2)  # Plotar os dois na mesma janela
