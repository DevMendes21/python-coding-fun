# Organizador de Tarefas Prioritárias

## 💡 Descrição do Desafio

Criar um script em Python que organize tarefas com níveis de prioridade e as ordene para execução. As tarefas devem ser ordenadas pela prioridade e pela data de criação.

## 🎯 Requisitos Básicos

1. **Classe Tarefa**: Implementar uma classe com os atributos:
   - Título
   - Descrição
   - Prioridade (1=alta, 2=média, 3=baixa)
   - Data de criação

2. **Armazenamento**: Armazenar as tarefas em uma lista.

3. **Ordenação**: Implementar uma função que liste as tarefas ordenadas por:
   - Prioridade (ascendente)
   - Data de criação (ascendente dentro de cada prioridade)

4. **Exibição**: Mostrar as tarefas formatadas com emojis indicando a prioridade.

## 🚀 Implementação

A implementação atual é uma versão ultra-compacta e otimizada que atende a todos os requisitos básicos.

### Tecnologias Utilizadas

- **Python 3.8+**
- **Módulos**: 
  - `dataclasses` para definição concisa da classe `Tarefa`
  - `enum.IntEnum` para representação elegante das prioridades
  - `datetime` para manipulação de datas

### Características da Implementação

- **Classe Tarefa**: Implementada como `@dataclass` com ordenação automática
- **Enum de Prioridade**: Com propriedades para emoji e nome textual
- **Ordenação Eficiente**: Usando o mecanismo interno de ordenação do Python
- **Interface Visual**: Formatação com emojis coloridos e layout organizado
- **Testes Integrados**: Verificação automatizada dos requisitos

## 📊 Exemplo de Uso

```python
from datetime import datetime
from organizador_tarefas import Tarefa, Prioridade, exibir_tarefas

# Criar tarefas
tarefas = [
    Tarefa("Revisão de código", "Analisar algoritmos", Prioridade.ALTA, datetime(2025, 7, 1)),
    Tarefa("Compras semanais", "Produtos orgânicos", Prioridade.BAIXA, datetime(2025, 7, 3)),
    Tarefa("Organizar workspace", "Limpar arquivos", Prioridade.MEDIA, datetime(2025, 7, 1))
]

# Exibir tarefas ordenadas
exibir_tarefas(tarefas)
```

## 🧪 Testes

O script inclui testes unitários básicos que verificam:

1. Criação correta de tarefas
2. Validação de prioridades inválidas
3. Ordenação correta por prioridade e data

Para executar os testes:

```bash
python organizador_tarefas.py --test
```

## 🔄 Possíveis Melhorias (Extras)

Funcionalidades que poderiam ser adicionadas em versões futuras:

1. **Persistência**: Salvar e carregar tarefas de um arquivo
2. **Interface de Usuário**: Adicionar tarefas via input do usuário
3. **Filtragem**: Filtrar tarefas por prioridade ou data
4. **Categorias**: Adicionar categorias às tarefas
5. **Status**: Adicionar status (pendente, em andamento, concluída)

## 📝 Notas de Otimização

A implementação atual foi otimizada para:

- **Concisão**: Código mínimo sem sacrificar legibilidade
- **Eficiência**: Ordenação automática e processamento otimizado
- **Robustez**: Validação de dados e tratamento de erros
- **Manutenibilidade**: Estrutura clara e bem documentada
