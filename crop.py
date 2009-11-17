import random

def mac(pessoas_com_carro, pessoas_sem_carro):
	p1 = pessoas_com_carro[random.randint(0,len(pessoas_com_carro)-1)]
	pessoas_com_carro.remove(p1)
	pessoas_total = pessoas_com_carro+pessoas_sem_carro
	p2 = pessoas_total[random.randint(0,len(pessoas_total)-1)]
	return (p1,p2)

def porta(pessoas):
	return pessoas[random.randint(0,len(pessoas)-1)]
