from datetime import datetime
from Evento import Evento
from EventoABC import DataHora
from EventoABC import EventoUnico
from EventoABC import EventoRecorrente

# Cria duas instâncias de Evento
evento1 = Evento(
    "Jujutsu Kaisen", 
    datetime(2025, 1, 10, 9, 0), 
    "Anime de acao, suspense etc. Foca em feiticeiros que buscam exorcizar maldicoes.", 
    True
)

evento2 = Evento(
    "Naruto", 
    datetime(2025, 1, 15, 14, 30), 
    "Anime de acao, suspense etc. Foca em ninja que realizao missoes para subir de rank.", 
    False
)

print("Evento 1:")
print(f"Titulo: {evento1.titulo}")
print(f"Data e Hora: {evento1.data_hora}")
print(f"Descricao: {evento1.descricao}")
print(f"Concluido: {evento1.is_concluido}")

print("\nEvento 2:")
print(f"Titulo: {evento2.titulo}")
print(f"Data e Hora: {evento2.data_hora}")
print(f"Descricao: {evento2.descricao}")
print(f"Concluido: {evento2.is_concluido}")

print("\nTotal de eventos criados:", Evento.total_eventos)


Teste_metodo = Evento(
    "The books on the table",
    datetime(2024, 7, 20, 22, 22),
    "Um livro que fala sobre um livro na mesa.",
    False
)
# Teste do Método de Instancia
Teste_metodo.isConcluido()

print("\nTeste metodo:")
print(f"Titulo: {Teste_metodo.titulo}")
print(f"Data e Hora: {Teste_metodo.data_hora}")
print(f"Descricao: {Teste_metodo.descricao}")
print(f"Concluido: {Teste_metodo.is_concluido}")

# teste do @classmethod
print("\nTotal de eventos criados:", Evento.num_eventos())

# Teste do @staticmethod
print("Validando Evento:", Evento.valida_evento(
    "The books on the table", 
    datetime(2024, 7, 20, 22, 19), 
    "Um livro que fala sobre um livro na mesa.",))

# Teste metodos magicos
print(evento1)
Metodos_magicos1 = Evento(
    "Uma noite fria",
    datetime(2024, 7, 20, 22, 22),
    "Um livro que fala sobre uma noite fria.",
    False
)

Metodos_magicos2 = Evento(
    "Uma noite quente",
    datetime(2024, 7, 20, 22, 22),
    "Um livro que fala sobre uma noite quente.",
    True
)

print(f"Teste de Comparacao de datas: {Metodos_magicos1.__eq__(Metodos_magicos2)}")
print(f"Teste de Comparacao de datas: {Metodos_magicos1.__ne__(Metodos_magicos2)}")
print(f"Teste de Comparacao de datas: {Metodos_magicos1.__lt__(Metodos_magicos2)}")
print(f"Teste de Comparacao de datas: {Metodos_magicos1.__le__(Metodos_magicos2)}")
print(f"Teste de Comparacao de datas: {Metodos_magicos1.__gt__(Metodos_magicos2)}")
print(f"Teste de Comparacao de datas: {Metodos_magicos1.__ge__(Metodos_magicos2)}")

# ------------------------------- Exercício Prático ------------------------------- #
dh = DataHora()
dh.data_hora = "15/02/2025, 14:30"

print(f"\nData definida: {dh.data_hora}")
print(f"Esta no passado? {dh.isPassado()}")
print(f"Data apos somar 365 dias: {dh.somaDias(365)}")
# Teste com data inválida
try:
    dh.data_hora = "2025-01-15 14:30"
except ValueError as e:
    print("Erro:", e)

# ------------------------------- Exercício 03 ------------------------------- #

# criar evento
evento = EventoUnico(
    'Reuniao',
    'Sala 302, predio da esquina',
    '05/10/2023, 16:30')

print(evento)
# editar data do evento (através da propriedade)
evento.editar_data_hora('05/10/2024, 16:30')
print(evento)

# ------------------------------- Exercício 04 ------------------------------- #

# criar evento
eventos = EventoRecorrente(
    'Reuniao',
    'Sala 302, predio da esquina',
    '05/01/2024, 16:30',
    '05/01/2025, 16:30',
    30)
print(f"\n{eventos}")

# editar um dos eventos
eventos.editar_data_hora(
    data_hora_antiga = '05/01/2024, 16:30',
    data_hora_nova = '05/12/2025, 11:30'
)
print(f"\n{eventos}")
print("-" * 80)  # Separador para facilitar a visualização

# ------------------------------- Exercício 05 ------------------------------- #
# EventoUnicos e EventoRecorrentes
lista_eventos = [
    EventoUnico(
        titulo = "Reuniao de Time",
        descricao = "Discutir metas do proximo trimestre.",
        data_hora = "20/01/2025, 09:00"
    ),
    EventoUnico(
        titulo = "Apresentacao de Projeto",
        descricao = "Apresentar o projeto final ao cliente.",
        data_hora = "22/01/2025, 14:00"
    ),
    EventoRecorrente(
        titulo = "Aula de futebol",
        descricao = "Aulas semanais de futebol para se tornar um egoista.",
        data_hora_inicial = "10/01/2025, 08:00",
        data_hora_final = "07/02/2025, 08:00",
        intervalo_repeticao = 7  # Uma vez por semana
    ),
    EventoRecorrente(
        titulo = "Revisao de Codigo",
        descricao = "Revisao mensal do codigo com a equipe.",
        data_hora_inicial = "05/01/2025, 10:00",
        data_hora_final = "05/06/2025, 10:00",
        intervalo_repeticao = 30  # Uma vez por mês
    )
]

for evento in lista_eventos:
    print(evento)
    print("-" * 80)  # Separador para facilitar a visualização
