import tkinter as tk
from tkinter import messagebox

class No:
    """
    Representa um nó na árvore binária.
    Armazena o valor, e referências para os filhos esquerdo e direito.
    """
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    """
    Classe responsável pela lógica da Árvore Binária de Busca (BST).
    """
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        """Método público para inserir um valor na árvore."""
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        """
        Lógica recursiva para encontrar a posição correta do novo valor.
        Menores vão para a esquerda, maiores para a direita.
        """
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)
        else:
            # Valor já existe, não duplicamos na BST simples
            pass

class AppArvore(tk.Tk):
    """
    Interface Gráfica usando Tkinter.
    """
    def __init__(self):
        super().__init__()
        self.title("Visualizador de Árvore Binária - Dev Júnior")
        self.geometry("800x600")
        
        self.arvore = ArvoreBinariaBusca()

        # --- Área de Controles ---
        frame_controles = tk.Frame(self)
        frame_controles.pack(pady=10)

        tk.Label(frame_controles, text="Insira números (separados por vírgula):").pack(side=tk.LEFT)
        
        self.entrada_dados = tk.Entry(frame_controles, width=30)
        self.entrada_dados.pack(side=tk.LEFT, padx=5)
        # Exemplo pré-preenchido para facilitar o teste
        self.entrada_dados.insert(0, "50, 30, 70, 20, 40, 60, 80")

        btn_gerar = tk.Button(frame_controles, text="Gerar Árvore", command=self.processar_entrada)
        btn_gerar.pack(side=tk.LEFT, padx=5)

        btn_limpar = tk.Button(frame_controles, text="Limpar", command=self.limpar_tudo)
        btn_limpar.pack(side=tk.LEFT, padx=5)

        # --- Canvas para Desenho ---
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def limpar_tudo(self):
        self.arvore = ArvoreBinariaBusca()
        self.canvas.delete("all")
        self.entrada_dados.delete(0, tk.END)

    def processar_entrada(self):
        """
        Lê a entrada do usuário, converte para lista de inteiros e monta a árvore.
        Aqui reside a lógica de tratamento de dados.
        """
        texto = self.entrada_dados.get()
        if not texto:
            return

        # Reinicia a árvore
        self.arvore = ArvoreBinariaBusca()
        self.canvas.delete("all")

        try:
            # CORREÇÃO/LÓGICA DE ENTRADA:
            # 1. Separa a string por vírgulas
            # 2. Remove espaços em branco (strip)
            # 3. Converte para inteiro
            valores = [int(v.strip()) for v in texto.split(',')]
            
            for val in valores:
                self.arvore.inserir(val)
            
            # Chama o desenho começando da raiz
            if self.arvore.raiz:
                self.desenhar_arvore(self.arvore.raiz, 400, 50, 200)
                
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira apenas números inteiros separados por vírgula.")

    def desenhar_arvore(self, no, x, y, distancia_x):
        """
        Desenha a árvore recursivamente no Canvas.
        x, y: coordenadas do centro do nó atual
        distancia_x: espaçamento horizontal entre filhos (diminui a cada nível)
        """
        raio = 20
        distancia_y = 60 # Distância vertical fixa entre níveis

        # Desenha conexão e chama recursão para Esquerda
        if no.esquerda:
            x_esq = x - distancia_x
            y_esq = y + distancia_y
            self.canvas.create_line(x, y, x_esq, y_esq, width=2)
            self.desenhar_arvore(no.esquerda, x_esq, y_esq, distancia_x / 2)

        # Desenha conexão e chama recursão para Direita
        if no.direita:
            x_dir = x + distancia_x
            y_dir = y + distancia_y
            self.canvas.create_line(x, y, x_dir, y_dir, width=2)
            self.desenhar_arvore(no.direita, x_dir, y_dir, distancia_x / 2)

        # Desenha o Nó (Círculo e Texto)
        # O nó é desenhado por último para ficar "por cima" das linhas
        self.canvas.create_oval(x - raio, y - raio, x + raio, y + raio, fill="lightblue", outline="black", width=2)
        self.canvas.create_text(x, y, text=str(no.valor), font=("Arial", 10, "bold"))

if __name__ == "__main__":
    app = AppArvore()
    app.mainloop()