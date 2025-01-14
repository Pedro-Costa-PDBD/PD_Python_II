from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class EventoABC(ABC):
    def __init__(self, _titulo: str, _descricao: str):
        self._titulo = _titulo
        self._descricao = _descricao
    
    @abstractmethod
    def __str__(self): pass

    @abstractmethod
    def isConcluido(self): pass

# ------------------------------- Exercício 02 ------------------------------- #
class DataHora:
    # Atributo de classe
    FORMAT = '%d/%m/%Y, %H:%M'

    def __init__(self):
        self._data_hora = None
    
    @property
    def data_hora(self):
        if self._data_hora:
            return self._data_hora.strftime(self.FORMAT)
        return None
    
    @data_hora.setter
    def data_hora(self, value: str):
        try:
            self._data_hora = datetime.strptime(value, self.FORMAT)
        except ValueError:
            raise ValueError(f"Data e hora invalidas. Use o formato: {self.FORMAT}")
    
    def isPassado(self):
        if self._data_hora:
            return self._data_hora < datetime.now()
        return False
    
    def somaDias(self, num_dias: int):
        if not self._data_hora:
            raise ValueError("A data/hora precisa ser definida antes de somar dias.")
        nova_data = self._data_hora + timedelta(days=num_dias)
        return nova_data.strftime(self.FORMAT)

# ------------------------------- Exercício 03 ------------------------------- #
class EventoUnico(EventoABC):
    def __init__(self, titulo: str, descricao: str, data_hora: str):
        super().__init__(titulo, descricao)
        self._data_hora = DataHora()
        self._data_hora.data_hora = data_hora

    def isConcluido(self):
        return self._data_hora.isPassado()
    
    def __str__(self):
        return (
            f"Evento: {self._titulo}, "
            f"Data: {self._data_hora.data_hora}, "
            f"Descricao: {self._descricao}, "
            f"Concluido: {self.isConcluido()}"
        )
    
    def editar_data_hora(self, string_alterada: str):
        try:
            self._data_hora.data_hora = string_alterada
        except ValueError as e:
            raise ValueError(f"Erro ao alterar data/hora: {e}")

# ------------------------------- Exercício 04 ------------------------------- #
class EventoRecorrente(EventoABC):
    def __init__(self, titulo: str, descricao: str, data_hora_inicial: str, data_hora_final: str, intervalo_repeticao: int):
        super().__init__(titulo, descricao)
        self._listDataHora = [] 

        data_inicio = DataHora()
        data_inicio.data_hora = data_hora_inicial

        data_final = DataHora()
        data_final.data_hora = data_hora_final

        while data_inicio._data_hora <= data_final._data_hora:
            self._listDataHora.append(data_inicio)
            data_inicio = DataHora()  # Criar nova instância para o próximo intervalo
            data_inicio.data_hora = self._listDataHora[-1].somaDias(intervalo_repeticao)

    def isConcluido(self, indice: int):
        if 0 <= indice < len(self._listDataHora):
            return self._listDataHora[indice].isPassado()
        raise IndexError("Índice fora do intervalo da lista de datas/horas.")

    def __str__(self):
        resultado = []
        for i, data_hora in enumerate(self._listDataHora):
            resultado.append(
                f"Evento: {self._titulo}, "
                f"Data: {data_hora.data_hora}, "
                f"Descricao: {self._descricao}, "
                f"Concluido: {self.isConcluido(i)}"
            )
        return "\n".join(resultado)

    def editar_data_hora(self, data_hora_antiga: str, data_hora_nova: str):

        for data_hora in self._listDataHora:
            if data_hora.data_hora == data_hora_antiga:
                try:
                    data_hora.data_hora = data_hora_nova
                    return
                except ValueError as e:
                    raise ValueError(f"Erro ao editar data/hora: {e}")
        # Caso não encontre nada
        raise ValueError(f"Data/hora antiga '{data_hora_antiga}' não encontrada na lista.")
