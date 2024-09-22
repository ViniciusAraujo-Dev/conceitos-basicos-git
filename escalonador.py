# classe do processo e seu construtor
class Processo:
    def __init__(self, id, tempo_execucao, prioridade=0):
        self.id = id
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade


# demais classes para os métodos de escalonamento

# primeiro a chegar, primeiro a ser executado
class FCFS:
    def escalonar(self, processos):
        tempo_total = 0
        for processo in processos:
            print(f"Processo {processo.id} iniciado. Tempo de execução: {processo.tempo_execucao}.")
            tempo_total += processo.tempo_execucao
            print(f"Processo {processo.id} finalizado. Tempo total: {tempo_total}.")

# menor tempo de execução é executado primeiro
class SJF:
    def escalonar(self, processos):
        processos.sort(key=lambda x: x.tempo_execucao)
        tempo_total = 0
        for processo in processos:
            print(f"Processo {processo.id} iniciado. Tempo de execução: {processo.tempo_execucao}.")
            tempo_total += processo.tempo_execucao
            print(f"Processo {processo.id} finalizado. Tempo total: {tempo_total}.")

# executado de acordo com a prioridade
class Prioridades:
    def escalonar(self, processos):
        processos.sort(key=lambda x: x.prioridade)
        tempo_total = 0
        for processo in processos:
            print(f"Processo {processo.id} iniciado. Tempo de execução: {processo.tempo_execucao}.")
            tempo_total += processo.tempo_execucao
            print(f"Processo {processo.id} finalizado. Tempo total: {tempo_total}.")

# usando os métodos com valores ficticios para simular 
if __name__ == "__main__":
    # Criação de processos
    processos = [
        Processo(id=1, tempo_execucao=5, prioridade=2),
        Processo(id=2, tempo_execucao=3, prioridade=1),
        Processo(id=3, tempo_execucao=8, prioridade=3)
    ]

    print("Escalonamento FCFS:")
    fcfs = FCFS()
    fcfs.escalonar(processos)

    print("\nEscalonamento SJF:")
    sjf = SJF()
    sjf.escalonar(processos)

    print("\nEscalonamento por Prioridade:")
    prioridades = Prioridades()
    prioridades.escalonar(processos)
