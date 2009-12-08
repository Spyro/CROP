import random

def mac(pessoas_com_carro, pessoas_sem_carro):
	return (pessoas_com_carro.pop(random.randint(0,len(pessoas_com_carro)-1)),random.choice(pessoas_com_carro+pessoas_sem_carro))

def porta(pessoas):
	return random.choice(pessoas)

def sorteiogrupos(participantes,groups):
	return [[participantes.pop(random.randint(0,len(participantes)-1)) for k in range(0,a)] for a in [int(len(participantes)/groups) + (((len(participantes)%groups) > i and 1) or 0) for i in range(0,groups)]]

# won't work with python 3.0
def cropsort(L):
	return map(lambda L: L if len(L)==1 else qsort([lt for lt in L[1:] if lt<L[0]]) + [L[0]] + qsort([ge for ge in L[1:] if ge >= L[0]]),[L])[0]
