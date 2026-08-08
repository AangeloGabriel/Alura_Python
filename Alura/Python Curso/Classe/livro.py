class livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} paginas'
    
    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'
    
    @property
    def paginas(self):
        return f'{self._paginas} paginas'
    
    @paginas.setter
    def paginas(self, valor):
        if valor < 0:
            raise ValueError('Numero de paginas nao pode ser menor que 0')
        self._paginas = valor    
    
Livro1 = livro('jose', 'maria', 56)

print(Livro1.paginas)