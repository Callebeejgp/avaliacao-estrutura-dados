Callebe de Almeida Sousa - RA: 02410041073

Kauan Lopes Bispo de Melo - RA: 02410041138

Ediglei Davi Alexandre de Sousa - RA: 02410041115

Taoã Augusto Martinelli de Araújo - RA: 0241004196

Gabriel Freire de Melo Santos - RA: 02410041149


📋 Descrição das Correções

Neste Pull Request, submeto as correções para os módulos de visualização de Árvore Binária e Grafos. O objetivo principal foi corrigir a lógica de entrada de dados e garantir que as estruturas fossem montadas corretamente na memória antes da renderização.

Principais Alterações:

Árvore Binária (ar.py):

Implementei a limpeza da entrada (strip) e conversão para inteiros.

Corrigi a lógica recursiva de inserção: valores menores à esquerda, maiores à direita. Antes, a árvore não respeitava a ordem de busca (BST).

Grafo (grafo.py):

Ajustei o parser de string para identificar o padrão Origem-Destino.

Utilizei um dicionário de adjacência para mapear as conexões bidirecionais (grafo não direcionado).

🧠 Raciocínio e Aprendizado

Durante o desenvolvimento, precisei relembrar a diferença teórica entre as duas estruturas:

Árvore: É hierárquica. O maior desafio foi visualizar a recursão na função inserir.

Grafo: É relacional. O desafio foi entender que, num grafo não direcionado, se A liga em B, B precisa ligar em A.

Uma dificuldade que encontrei foi manipular as coordenadas do canvas no Tkinter para que os nós não ficassem sobrepostos. Resolvi isso usando uma distribuição matemática (círculo trigonométrico para o grafo e espaçamento dinâmico para a árvore).

🤖 Uso de Inteligência Artificial

Para concluir esta tarefa, utilizei IA (Gemini/ChatGPT) de forma consultiva.

Prompt 1: "Como posso dividir uma string 'A-B' em Python para pegar as duas letras separadamente?"

Aplicação: Usei a explicação sobre o método .split('-') para corrigir a leitura dos dados no arquivo do grafo.

Prompt 2: "Explique a lógica de desenhar uma árvore binária recursivamente em um canvas."

Aplicação: A IA me ajudou a entender que eu precisava passar as coordenadas X e Y como argumentos na recursão, diminuindo o espaçamento a cada nível.

Este PR faz parte da atividade avaliativa de Estrutura de Dados.