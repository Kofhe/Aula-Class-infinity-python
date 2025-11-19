class Autor:
    def __init__(self,nome,data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

class Biblioteca:
    def __init__(self):
        self.catalogo_livros = []
        self.lista_membros = []
        
class Livro:
    def __init__(self, titulo, anoPub,autor:Autor):
        self.titulo = titulo
        self.anoPub = anoPub
        self.autor = autor

a1 = Autor(nome="CS Lewis",data_nascimento="13/05/1880")
l1 = Livro("Como para de ser noob no clash",2025,a1)

print(l1.titulo)
print(l1.anoPub)
print(l1.autor.nome)
print(l1.autor.data_nascimento)
