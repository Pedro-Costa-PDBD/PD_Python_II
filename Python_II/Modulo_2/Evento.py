from datetime import datetime

class Evento:
    # Atributo de classe
    total_eventos = 0

    def __init__(self, titulo: str, data_hora: datetime, descricao: str, is_concluido: bool):
        # Atributos de instância
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = is_concluido

        # Contador de eventos
        if(self.is_concluido) == True:
            Evento.total_eventos += 1

    # Método de Instancia
    def isConcluido(self):
        if self.data_hora < datetime.now():
            self.is_concluido = True
    
    @classmethod
    def num_eventos(cls):
        return cls.total_eventos
    
    @staticmethod
    def valida_evento(titulo: str, data_hora: datetime, descricao: str):
        return isinstance(titulo, str) and isinstance(data_hora, datetime) and isinstance(descricao, str)
    
    # Métodos Mágicos
    def __str__(self,):
        return f"Evento: {self.titulo}, Data: {self.data_hora}, Descricao: {self.descricao}, Concluido: {self.is_concluido}"
    
    def __eq__(self, other): return self.data_hora == other.data_hora
    def __ne__(self, other): return self.data_hora != other.data_hora
    def __lt__(self, other): return self.data_hora < other.data_hora
    def __le__(self, other): return self.data_hora <= other.data_hora
    def __gt__(self, other): return self.data_hora > other.data_hora
    def __ge__(self, other): return self.data_hora >= other.data_hora

