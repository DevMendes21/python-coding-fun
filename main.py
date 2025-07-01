"""
💡 Desafio Diário: Organizador de Tarefas Prioritárias

🎯 Objetivo:
Crie um script em Python que leia uma lista de tarefas com níveis de prioridade 
e organize-as para execução. As tarefas devem ser ordenadas pela prioridade e pela data de criação.

📋 Requisitos:

1. Crie uma classe `Tarefa` com os seguintes atributos:
   - `titulo` (str)
   - `descricao` (str)
   - `prioridade` (int) → onde 1 = alta, 2 = média, 3 = baixa
   - `data_criacao` (datetime)

2. Armazene as tarefas em uma lista.

3. Crie uma função `listar_tarefas_ordenadas()` que:
   - Retorne as tarefas ordenadas por:
     - Prioridade (crescente)
     - Data de criação (mais antiga primeiro)

4. Exiba as tarefas ordenadas no seguinte formato:
   [1] 🔴 2024-07-01 - Estudar algoritmos (Estudar ordenação e busca binária)
   [2] 🟡 2024-07-01 - Limpar a caixa de e-mail (Arquivar mensagens antigas)
   [3] 🟢 2024-07-02 - Comprar frutas (Banana, maçã, laranja)

🔁 Extras (opcionais):
- Adicione persistência com arquivo .json ou .csv.
- Permita adicionar novas tarefas via input().
- Adicione um filtro para exibir apenas tarefas de determinada prioridade.

📦 Exemplo de uso (mock de entrada):
tarefas = [
    Tarefa("Estudar algoritmos", "Estudar ordenação e busca binária", 1, datetime(2024, 7, 1)),
    Tarefa("Comprar frutas", "Banana, maçã, laranja", 3, datetime(2024, 7, 2)),
    Tarefa("Limpar a caixa de e-mail", "Arquivar mensagens antigas", 2, datetime(2024, 7, 1)),
]

💡 Dica:
Você pode usar `sorted()` com lambda ou implementar `__lt__` na classe `Tarefa`.
"""
