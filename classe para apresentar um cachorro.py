# faça uma classe para presentar um cachorro
# Caracteristicas
# nome
# cor
# raca

Class Dog:
    def __init__(self,nome,cor,raça): #init = iniciar a classe
        self.nome = nome 
        self.cor = cor
        self.raça = raça
    def latir(self):
        return "auau"
#objeto daclasse dog
dog1 = Dog(nome="Totó",cor="caramelo",raça="indefinida")
print(dog1)
print(dog1.latir())

