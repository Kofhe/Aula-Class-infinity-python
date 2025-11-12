class Animal:
    def __init__(self,nome,cor):
        self.nome = nome 
        self.cor = cor 

class Cachorro(Animal):
    def __init__(self,nome,cor):
   #o super herdar caracteristiscas da classe superior
        super().__init__(nome,cor)

class Gato(Animal):
    def __init__(self,nome,cor):
   #o super herdar caracteristiscas da classe superior
        super().__init__(nome,cor)

Gato1 = Gato(nome="Batman",cor="Frajola")
Cachorro1 = Cachorro(nome="Totó",cor="caramelo")
print(vars(Cachorro1))
print(vars(Gato1))
