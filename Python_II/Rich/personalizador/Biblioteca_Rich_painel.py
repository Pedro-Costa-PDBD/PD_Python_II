from rich.console import Console
from rich.panel import Panel

console = Console()

def exibir_painel(texto: str, is_arquivo: bool):
    """
    Exibe o texto formatado como um painel.
    """
    if is_arquivo:
        with open(texto, "r") as file:
            texto = file.read()
    console.print(Panel(texto, title="Painel", subtitle="Rodapé"))


def exibir_painel_alerta(texto: str, is_arquivo: bool):
    """
    Exibe o texto em um painel com estilo de alerta.
    """
    if is_arquivo:
        with open(texto, "r") as file:
            texto = file.read()
    console.print(Panel(texto, title="⚠ ALERTA ⚠", border_style="bold red"))