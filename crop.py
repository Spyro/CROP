import random

def mac(pessoas_com_carro, pessoas_sem_carro):
	p1 = random.choice(pessoas_com_carro)
	pessoas_com_carro.remove(p1)
	pessoas_total = pessoas_com_carro+pessoas_sem_carro
	p2 = random.choice(pessoas_total)
	return (p1,p2)

def porta(pessoas):
	return random.choice(pessoas)
