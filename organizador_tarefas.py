"""
Organizador de Tarefas Prioritárias v1.0 - Versão ultra-compacta
"""

from datetime import datetime, timedelta
from typing import List, Tuple
from dataclasses import dataclass, field
from enum import IntEnum
import sys


class Prioridade(IntEnum):
    """Níveis de prioridade com propriedades visuais."""
    ALTA, MEDIA, BAIXA = 1, 2, 3
    
    @property
    def emoji(self) -> str: return ["🔴", "🟡", "🟢"][self-1]
    
    @property
    def nome(self) -> str: return ["Alta", "Média", "Baixa"][self-1]


@dataclass(order=True, frozen=True)
class Tarefa:
    """Tarefa com ordenação automática por prioridade e data."""
    sort_index: Tuple[int, datetime] = field(init=False, repr=False, compare=True, hash=False)
    titulo: str
    descricao: str
    prioridade: Prioridade
    data_criacao: datetime
    
    def __post_init__(self):
        if not self.titulo.strip(): raise ValueError("Título vazio")
        p = Prioridade(self.prioridade) if isinstance(self.prioridade, int) else self.prioridade
        object.__setattr__(self, 'prioridade', p)
        object.__setattr__(self, 'sort_index', (p.value, self.data_criacao))
    
    def __str__(self):
        return f"{self.prioridade.emoji} {self.data_criacao.strftime('%Y-%m-%d')} - {self.titulo} ({self.descricao})"


def exibir_tarefas(tarefas: List[Tarefa]) -> None:
    """Exibe tarefas ordenadas com formatação visual."""
    tarefas_ordenadas = sorted(tarefas) if tarefas else []
    
    if not tarefas_ordenadas:
        print("\n📋 Sem tarefas\n")
        return
    
    # Exibição minimalista e eficiente
    print(f"\n{'=' * 40}\nTAREFAS PRIORITÁRIAS\n{'=' * 40}")
    print(f"\n🔴 Alta | 🟡 Média | 🟢 Baixa\n{'-' * 40}")
    
    # Lista numerada de tarefas
    for i, t in enumerate(tarefas_ordenadas, 1):
        print(f"[{i}] {t}")
    print(f"{'-' * 40}\n{len(tarefas_ordenadas)} tarefa(s)\n")


def executar_testes():
    """Executa testes básicos e exibe resultados."""
    print("TESTES UNITÁRIOS\n" + "-" * 20)
    resultados = []
    
    # Teste 1: Criação
    try:
        t = Tarefa("Teste", "Descrição", Prioridade.MEDIA, datetime.now())
        assert t.titulo == "Teste" and t.prioridade == Prioridade.MEDIA
        resultados.append(("✅", "Criação básica"))
    except Exception as e:
        resultados.append(("❌", f"Falha na criação: {e}"))
    
    # Teste 2: Validação
    try:
        Tarefa("Teste", "Descrição", 5, datetime.now())
        resultados.append(("❌", "Aceitou prioridade inválida"))
    except ValueError:
        resultados.append(("✅", "Rejeitou prioridade inválida"))
    
    # Teste 3: Ordenação
    hoje = datetime.now()
    tarefas = [
        Tarefa("Alta hoje", "Desc", Prioridade.ALTA, hoje),
        Tarefa("Alta ontem", "Desc", Prioridade.ALTA, hoje - timedelta(days=1))
    ]
    ordenadas = sorted(tarefas)
    if ordenadas[0].data_criacao < ordenadas[1].data_criacao:
        resultados.append(("✅", "Ordenação correta"))
    else:
        resultados.append(("❌", "Ordenação incorreta"))
    
    # Exibe resultados
    for status, msg in resultados:
        print(f"{status} {msg}")
    
    print(f"\nRESUMO: {sum(1 for s, _ in resultados if s == '✅')}/{len(resultados)} testes OK\n")


# Ponto de entrada com tratamento de erros
if __name__ == "__main__":
    try:
        # Modo de teste
        if len(sys.argv) > 1 and sys.argv[1] == "--test":
            executar_testes()
        else:
            # Tarefas de exemplo usei o inline para maior concisão
            exibir_tarefas([
                Tarefa("Revisão de código", "Analisar algoritmos de ML", Prioridade.ALTA, datetime(2025, 7, 1)),
                Tarefa("Compras semanais", "Produtos orgânicos e itens de casa", Prioridade.BAIXA, datetime(2025, 7, 3)),
                Tarefa("Organizar workspace", "Limpar arquivos temporários", Prioridade.MEDIA, datetime(2025, 7, 1)),
                Tarefa("Preparar apresentação Q3", "Dashboard de resultados", Prioridade.ALTA, datetime(2025, 7, 2)),
                Tarefa("Agendar manutenção VR", "Atualização de firmware", Prioridade.MEDIA, datetime(2025, 7, 2))
            ])
    except KeyboardInterrupt:
        print("\n❌ Programa interrompido")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        sys.exit(1)
