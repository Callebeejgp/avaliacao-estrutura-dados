import tkinter as tk
from tkinter import messagebox
import math

class Grafo:
    """
    Representação do grafo usando Lista de Adjacência (Dicionário).
    Chave: Nome do nó
    Valor: Lista de vizinhos
    """
    def __init__(self):
        self.adjacencia = {}

    def adicionar_aresta(self, u, v):
        """
        Adiciona uma conexão entre u e v.
        Como é não-direcionado, adiciona nos dois sentidos.
        """
        # Garante que os nós existam no dicionário
        if u not in self.adjacencia:
            self.adjacencia[u] = []
        if v not in self.adjacencia:
            self.adjacencia[v] = []

        # Adiciona conexão se não existir (evita duplicatas)
        if v not in self.adjacencia[u]:
            self.adjacencia[u].append(v)
        if u not in self.adjacencia[v]:
            self.adjacencia[v].append(u)

class AppGrafo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Visualizador de Grafos - Dev Júnior")
        self.geometry("800x600")
        
        self.grafo = Grafo()

        # --- Controles ---
        frame_top = tk.Frame(self)
        frame_top.pack(pady=10)

        tk.Label(frame_top, text="Arestas (ex: A-B, B-C):").pack(side=tk.LEFT)
        self.entry_arestas = tk.Entry(frame_top, width=40)
        self.entry_arestas.pack(side=tk.LEFT, padx=5)
        self.entry_arestas.insert(0, "A-B, B-C, C-A, B-D, D-E, E-B")

        btn_draw = tk.Button(frame_top, text="Renderizar Grafo", command=self.processar_grafo)
        btn_draw.pack(side=tk.LEFT, padx=5)

        # --- Canvas ---
        self.canvas = tk.Canvas(self, bg="#f0f0f0")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def processar_grafo(self):
        """
        Interpreta a string de entrada e constrói a estrutura do grafo.
        """
        entrada = self.entry_arestas.get()
        if not entrada:
            return

        self.grafo = Grafo()
        self.canvas.delete("all")

        try:
            # Divide pares por vírgula: ["A-B", " B-C"]
            pares = entrada.split(',')
            
            for par in pares:
                par = par.strip()
                if '-' in par:
                    # LÓGICA DE PARSING: Divide "A-B" em u="A", v="B"
                    u, v = par.split('-')
                    self.grafo.adicionar_aresta(u.strip(), v.strip())
            
            self.desenhar_grafo_circular()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Formato inválido: {e}")

    def desenhar_grafo_circular(self):
        """
        Algoritmo simples para distribuir nós em um círculo.
        Facilita a visualização sem precisar de bibliotecas complexas como networkx.
        """
        nos = list(self.grafo.adjacencia.keys())
        n = len(nos)
        if n == 0: return

        # Parâmetros do layout
        centro_x, centro_y = 400, 300
        raio_circulo = 200
        raio_no = 20
        
        coords = {} # Armazena (x, y) de cada nó

        # 1. Calcular posições (Matemática: Coordenadas Polares -> Cartesianas)
        angulo_passo = (2 * math.pi) / n
        for i, no in enumerate(nos):
            angulo = i * angulo_passo
            x = centro_x + raio_circulo * math.cos(angulo)
            y = centro_y + raio_circulo * math.sin(angulo)
            coords[no] = (x, y)

        # 2. Desenhar Arestas (linhas)
        # Usamos um set para não desenhar a mesma linha duas vezes (A-B e B-A)
        arestas_desenhadas = set()
        
        for u in nos:
            x1, y1 = coords[u]
            for v in self.grafo.adjacencia[u]:
                # Ordena para garantir que A-B seja igual a B-A na checagem
                chave_aresta = tuple(sorted((u, v)))
                
                if chave_aresta not in arestas_desenhadas:
                    x2, y2 = coords[v]
                    self.canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)
                    arestas_desenhadas.add(chave_aresta)

        # 3. Desenhar Nós (círculos) por cima das linhas
        for no in nos:
            x, y = coords[no]
            color = "#ffcc00" # Amarelo/Laranja
            
            self.canvas.create_oval(x - raio_no, y - raio_no, x + raio_no, y + raio_no, 
                                    fill=color, outline="black", width=2)
            self.canvas.create_text(x, y, text=no, font=("Arial", 12, "bold"))

if __name__ == "__main__":
    app = AppGrafo()
    app.mainloop()