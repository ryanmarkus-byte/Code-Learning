class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def detalhes(self):
        print(f"O livro {self.titulo} foi escrito por {self.autor} e tem {self.paginas} paginas.")

meu_livro = Livro("Chuva de fogo", "Leonardo L. Mello", 378)
outro_livro = Livro("Daydream", "Leonardo L. Mello", 250)

meu_livro.detalhes()
outro_livro.detalhes()