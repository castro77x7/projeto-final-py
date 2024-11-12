import tkinter as tk
from tkinter import messagebox
import pygame

# Inicializar o Pygame para reproduzir música
pygame.mixer.init()
pygame.mixer.music.load("audio-magic.mp3")
pygame.mixer.music.play(-1)  # -1 para tocar em loop

# Classe Livro
class Livro:
    def __init__(self, titulo, autor, genero, ano, descricao):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ano = ano
        self.descricao = descricao
    
    def compartilhar_historia(self):
        return f'O livro "{self.titulo}" compartilha uma história mágica: {self.descricao}'
    
    def mostrar_info(self):
        return f'Título: {self.titulo}\nAutor: {self.autor}\nGênero: {self.genero}\nAno: {self.ano}\nDescrição: {self.descricao}\n'

# Classe Livraria
class Livraria:
    def __init__(self):
        self.catalogo = []
    
    def adicionar_livro(self, livro):
        self.catalogo.append(livro)
    
    def obter_catalogo(self):
        return "\n\n".join([livro.mostrar_info() for livro in self.catalogo])
    
    def buscar_por_genero(self, genero):
        livros_genero = [livro.mostrar_info() for livro in self.catalogo if livro.genero.lower() == genero.lower()]
        return "\n\n".join(livros_genero) if livros_genero else "Nenhum livro encontrado nesse gênero."
    
    def remover_livro(self, titulo):
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo.lower():
                self.catalogo.remove(livro)
                return f'O livro "{titulo}" foi removido do catálogo.'
        return "Livro não encontrado."

# Classe Bibliotecario
class Bibliotecario:
    def __init__(self, nome, livraria):
        self.nome = nome
        self.livraria = livraria
    
    def adicionar_livro(self, livro):
        self.livraria.adicionar_livro(livro)
    
    def exibir_historia(self, titulo):
        for livro in self.livraria.catalogo:
            if livro.titulo.lower() == titulo.lower():
                return livro.compartilhar_historia()
        return "Livro não encontrado."

# Função para exibir o catálogo de livros
def exibir_catalogo():
    catalogo_texto = biblioteca.obter_catalogo()
    if catalogo_texto:
        messagebox.showinfo("Catálogo de Livros", catalogo_texto)
    else:
        messagebox.showinfo("Catálogo de Livros", "O catálogo está vazio.")

# Função para adicionar um novo livro
def adicionar_livro():
    titulo = titulo_entry.get()
    autor = autor_entry.get()
    genero = genero_entry.get()
    ano = ano_entry.get()
    descricao = descricao_entry.get()
    
    # Verificação básica de entrada
    if titulo and autor and genero and ano and descricao:
        try:
            int(ano)  # Verifica se o ano é um número
            novo_livro = Livro(titulo, autor, genero, ano, descricao)
            sr_code.adicionar_livro(novo_livro)
            messagebox.showinfo("Sucesso", f"O livro '{titulo}' foi adicionado!")
            
            # Limpar os campos de entrada
            titulo_entry.delete(0, tk.END)
            autor_entry.delete(0, tk.END)
            genero_entry.delete(0, tk.END)
            ano_entry.delete(0, tk.END)
            descricao_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showwarning("Erro", "O campo 'Ano' deve ser um número.")
    else:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

# Função para buscar livros por gênero
def buscar_por_genero():
    genero = genero_entry.get()
    if genero:
        livros_genero = biblioteca.buscar_por_genero(genero)
        messagebox.showinfo("Livros por Gênero", livros_genero)
    else:
        messagebox.showwarning("Aviso", "Por favor, insira um gênero para busca.")

# Função para compartilhar a história de um livro específico
def compartilhar_historia():
    titulo = titulo_entry.get()
    if titulo:
        historia = sr_code.exibir_historia(titulo)
        messagebox.showinfo("História do Livro", historia)
    else:
        messagebox.showwarning("Aviso", "Por favor, insira o título do livro.")

# Função para remover um livro
def remover_livro():
    titulo = titulo_entry.get()
    if titulo:
        resultado = biblioteca.remover_livro(titulo)
        messagebox.showinfo("Remover Livro", resultado)
    else:
        messagebox.showwarning("Aviso", "Por favor, insira o título do livro.")

# Função para fechar o programa e parar a música
def on_closing():
    pygame.mixer.music.stop()
    root.destroy()

# Criação da janela principal
root = tk.Tk()
root.title("Magic Books - Sistema de Livraria")
root.geometry("400x500")
root.configure(bg="#f0e6d2")  # Cor de fundo para dar um toque mágico
root.protocol("WM_DELETE_WINDOW", on_closing)

biblioteca = Livraria()
sr_code = Bibliotecario("Mr. Code", biblioteca)

# Elementos da interface para entrada de dados dos livros
tk.Label(root, text="Título:", bg="#f0e6d2").pack()
titulo_entry = tk.Entry(root)
titulo_entry.pack()

tk.Label(root, text="Autor:", bg="#f0e6d2").pack()
autor_entry = tk.Entry(root)
autor_entry.pack()

tk.Label(root, text="Gênero:", bg="#f0e6d2").pack()
genero_entry = tk.Entry(root)
genero_entry.pack()

tk.Label(root, text="Ano:", bg="#f0e6d2").pack()
ano_entry = tk.Entry(root)
ano_entry.pack()

tk.Label(root, text="Descrição:", bg="#f0e6d2").pack()
descricao_entry = tk.Entry(root)
descricao_entry.pack()

# Botões para operações
adicionar_btn = tk.Button(root, text="Adicionar Livro", command=adicionar_livro, bg="#4caf50", fg="white")
adicionar_btn.pack(pady=5)

compartilhar_btn = tk.Button(root, text="Compartilhar História", command=compartilhar_historia, bg="#ff9800", fg="white")
compartilhar_btn.pack(pady=5)

buscar_btn = tk.Button(root, text="Buscar por Gênero", command=buscar_por_genero, bg="#009688", fg="white")
buscar_btn.pack(pady=5)

remover_btn = tk.Button(root, text="Remover Livro", command=remover_livro, bg="#f44336", fg="white")
remover_btn.pack(pady=5)

catalogo_btn = tk.Button(root, text="Exibir Catálogo", command=exibir_catalogo, bg="#2196f3", fg="white")
catalogo_btn.pack(pady=5)

# Iniciar o loop principal da interface Tkinter
root.mainloop()
