from datetime import datetime
from Evento import Evento

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