# Exercicio 2.8
#
# Pedro Paulo Herzog Junior		10284692
# Samuel Libardi Godoy			9805891
# Vinicius Molina Garcia		8929296

# Este script gera uma simulação FDTD de uma onda eletromagnetica unidimensional
# dado que o espaço pode ser repartido em multiplas seções com diferentes S (numero de Courant - Taflove eq 2.28a)
# de acordo com a descrição do método publicada no Taflove

CONST_c = 299792458  # VELOCIDADE DA LUZ NO VACUO EM m/s


def fdtd_gen(f_fonte, dt, partes_espaco):
	""" Cria um gerador para a simulação FDTD
	Este gerador retorna a cada passo uma iteração no tempo (n) da simulação FDTD

	parametros:
	f_fonte: função no tempo (t) da fonte geradora, posicionada no ponto 0
	dt: tamanho do passo temporal
	partes_espaco: partição do espaço: lista de tuplas da forma (numero de celulas, S)
	"""
	# Calcular o tamanho total do espaço, dado que o ponto inicial e final 
	# não pertencem a nenhuma das partições
	len_tot = sum(len_part for len_part, S in partes_espaco) + 2

	# inicializa os passos n e n-1
	step_nm1 = [0 for i in range(len_tot)]
	step_n = [f_fonte(0)] + [0 for i in range(len_tot - 1)]
	n = 0  #contador de passos (necessario para obter o valor da fonte no tempo t)

	# pré-processamento do espaço:
	# transforma a lista de (tamanho, S)
	# em uma lista de (inicio, fim, S**2), que auxilia nas iterações
	len_acc = 1
	partes_param = []
	for len_parte, S in partes_espaco:
		partes_param.append((len_acc, len_acc + len_parte, S ** 2))
		len_acc = len_acc + len_parte

	# Realiza as iterações
	while True:
		yield step_n

		n = n + 1
		step = (
			[f_fonte(n*dt)]  # Valor da fonte no tempo t
			+ [_fdtd_ponto(i, step_n, step_nm1, S2) for inic_parte, fim_parte, S2 in partes_param for i in range(inic_parte, fim_parte)]  # calcula cada ponto da proxima iteração para todas as partições do espaço
			+ [0] # O ultimo ponto é sempre 0 (contorno)
		)
		step_nm1 = step_n
		step_n = step

def _fdtd_ponto(i, un, unm1, S2):
	""" Função (interna) que calcula o próximo passo (n+1) para um ponto especifico

	Parametros:
	i: posição i no grid de simulação
	un: valores de u do passo n da iteração
	unm1: valores de u do passo n-1 da iteração
	"""

	if S2 == 1: return un[i + 1] + un[i - 1] - unm1[i]  # Caso para magic timestep
	else: return S2 * (un[i+1] - un[i] - un[i] + un[i-1]) + un[i] + un[i] - unm1[i]  # Caso geral
